import os.path as osp
from typing import Any, Dict

import json
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image

from modelscope.metainfo import Models
from modelscope.models.base import Model
from modelscope.models.builder import MODELS
from modelscope.models.multi_modal.imagen.diffusion import (GaussianDiffusion,
                                                            beta_schedule)
from modelscope.models.multi_modal.imagen.structbert import (BertConfig,
                                                             BertModel)
from modelscope.models.multi_modal.imagen.tokenizer import FullTokenizer
from modelscope.models.multi_modal.imagen.unet_generator import ImagenGenerator
from modelscope.models.multi_modal.imagen.unet_imagen_upsampler_256 import \
    SuperResUNet256
from modelscope.models.multi_modal.imagen.unet_upsampler_1024 import \
    ImagenUpsampler1024
from modelscope.utils.constant import ModelFile, Tasks
from modelscope.utils.logger import get_logger

logger = get_logger()

__all__ = ['ImagenForTextToImageSynthesis']


def make_diffusion(schedule,
                   num_timesteps=1000,
                   init_beta=None,
                   last_beta=None,
                   var_type='fixed_small'):
    betas = beta_schedule(schedule, num_timesteps, init_beta, last_beta)
    diffusion = GaussianDiffusion(betas, var_type=var_type)
    return diffusion


class Tokenizer(object):

    def __init__(self, vocab_file, seq_len=64):
        self.vocab_file = vocab_file
        self.seq_len = seq_len
        self.tokenizer = FullTokenizer(
            vocab_file=vocab_file, do_lower_case=True)

    def __call__(self, text):
        # tokenization
        tokens = self.tokenizer.tokenize(text)
        tokens = ['[CLS]'] + tokens[:self.seq_len - 2] + ['[SEP]']
        input_ids = self.tokenizer.convert_tokens_to_ids(tokens)
        input_mask = [1] * len(input_ids)
        segment_ids = [0] * len(input_ids)

        # padding
        input_ids += [0] * (self.seq_len - len(input_ids))
        input_mask += [0] * (self.seq_len - len(input_mask))
        segment_ids += [0] * (self.seq_len - len(segment_ids))
        assert len(input_ids) == len(input_mask) == len(
            segment_ids) == self.seq_len

        # convert to tensors
        input_ids = torch.LongTensor(input_ids)
        input_mask = torch.LongTensor(input_mask)
        segment_ids = torch.LongTensor(segment_ids)
        return input_ids, segment_ids, input_mask


class ImagenModel(nn.Module):

    def __init__(self, model_dir):
        super(ImagenModel, self).__init__()
        # including text and generator config
        model_config = json.load(
            open('{}/imagen_config.json'.format(model_dir)))

        # text encoder
        text_config = model_config['text_config']
        self.text_encoder = BertModel(BertConfig.from_dict(text_config))

        # generator (64x64)
        generator_config = model_config['generator_config']
        self.unet_generator = ImagenGenerator(**generator_config)

        # imagen upsampler (256x256)
        imagen_upsampler_256_config = model_config[
            'imagen_upsampler_256_config']
        self.unet_imagen_upsampler_256 = SuperResUNet256(
            **imagen_upsampler_256_config)

        # dalle2 upsampler (1024x1024)
        upsampler_1024_config = model_config['upsampler_1024_config']
        self.unet_upsampler_1024 = ImagenUpsampler1024(**upsampler_1024_config)

    def forward(self, noise, timesteps, input_ids, token_type_ids,
                attention_mask):
        context, y = self.text_encoder(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            attention_mask=attention_mask)
        context = context[-1]
        x = self.unet_generator(noise, timesteps, y, context, attention_mask)
        x = self.unet_imagen_upsampler_256(noise, timesteps, x,
                                           torch.zeros_like(timesteps), y,
                                           context, attention_mask)
        x = self.unet_upsampler_1024(x, t, x)
        return x


@MODELS.register_module(
    Tasks.text_to_image_synthesis, module_name=Models.imagen)
class ImagenForTextToImageSynthesis(Model):

    def __init__(self, model_dir, device_id=-1):
        super().__init__(model_dir=model_dir, device_id=device_id)
        imagen_model = ImagenModel(model_dir=model_dir)
        pretrained_params = torch.load(
            osp.join(model_dir, ModelFile.TORCH_MODEL_BIN_FILE), 'cpu')
        imagen_model.load_state_dict(pretrained_params)
        imagen_model.eval()

        self.device_id = device_id
        if self.device_id >= 0:
            self.device = torch.device(f'cuda:{self.device_id}')
            imagen_model.to('cuda:{}'.format(self.device_id))
            logger.info('Use GPU: {}'.format(self.device_id))
        else:
            self.device = torch.device('cpu')
            logger.info('Use CPU for inference')

        # modules
        self.text_encoder = imagen_model.text_encoder
        self.unet_generator = imagen_model.unet_generator
        self.unet_imagen_upsampler_256 = imagen_model.unet_imagen_upsampler_256
        self.unet_upsampler_1024 = imagen_model.unet_upsampler_1024

        # text tokenizer
        vocab_path = '{}/vocab.txt'.format(model_dir)
        self.tokenizer = Tokenizer(vocab_file=vocab_path, seq_len=64)

        # diffusion process
        diffusion_params = json.load(
            open('{}/diffusion_config.json'.format(model_dir)))
        self.diffusion_generator = make_diffusion(
            **diffusion_params['generator_config'])
        self.diffusion_imagen_upsampler_256 = make_diffusion(
            **diffusion_params['imagen_upsampler_256_config'])
        self.diffusion_upsampler_1024 = make_diffusion(
            **diffusion_params['upsampler_1024_config'])

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if not all([key in input for key in ('text', 'noise', 'timesteps')]):
            raise ValueError(
                f'input should contains "text", "noise", and "timesteps", but got {input.keys()}'
            )
        input_ids, token_type_ids, attention_mask = self.tokenizer(
            input['text'])
        input_ids = input_ids.to(self.device).unsqueeze(0)
        token_type_ids = token_type_ids.to(self.device).unsqueeze(0)
        attention_mask = attention_mask.to(self.device).unsqueeze(0)
        context, y = self.text_encoder(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            attention_mask=attention_mask)
        context = context[-1]
        x = self.unet_generator(noise, timesteps, y, context, attention_mask)
        x = self.unet_imagen_upsampler_256(noise, timesteps, x,
                                           torch.zeros_like(timesteps), y,
                                           context, attention_mask)
        x = self.unet_upsampler_1024(x, t, x)
        img = x.clamp(-1, 1).add(1).mul(127.5)
        img = img.squeeze(0).permute(1, 2, 0).cpu().numpy().astype(np.uint8)
        return img

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs

    @torch.no_grad()
    def generate(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if 'text' not in input:
            raise ValueError(
                f'input should contain "text", but got {input.keys()}')

        # encode text
        input_ids, token_type_ids, attention_mask = self.tokenizer(
            input['text'])
        input_ids = input_ids.to(self.device).unsqueeze(0)
        token_type_ids = token_type_ids.to(self.device).unsqueeze(0)
        attention_mask = attention_mask.to(self.device).unsqueeze(0)
        context, y = self.text_encoder(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            attention_mask=attention_mask)
        context = context[-1]

        # generation
        img = self.diffusion_generator.ddim_sample_loop(
            noise=torch.randn(1, 3, 64, 64).to(self.device),
            model=self.unet_generator,
            model_kwargs=[{
                'y': y,
                'context': context,
                'mask': attention_mask
            }, {
                'y': torch.zeros_like(y),
                'context': torch.zeros_like(context),
                'mask': attention_mask
            }],
            percentile=input.get('generator_percentile', 0.995),
            guide_scale=input.get('generator_guide_scale', 5.0),
            ddim_timesteps=input.get('generator_ddim_timesteps', 250),
            eta=input.get('generator_ddim_eta', 0.0))

        # upsampling (64->256)
        img = F.interpolate(
            img, scale_factor=4.0, mode='bilinear', align_corners=False)
        img = self.diffusion_imagen_upsampler_256.ddim_sample_loop(
            noise=torch.randn_like(img),
            model=self.unet_imagen_upsampler_256,
            model_kwargs=[{
                'lx': img,
                'lt': torch.zeros(1).to(self.device),
                'y': y,
                'context': context,
                'mask': attention_mask
            }, {
                'lx': img,
                'lt': torch.zeros(1).to(self.device),
                'y': torch.zeros_like(y),
                'context': torch.zeros_like(context),
                'mask': torch.zeros_like(attention_mask)
            }],
            percentile=input.get('generator_percentile', 0.995),
            guide_scale=input.get('generator_guide_scale', 5.0),
            ddim_timesteps=input.get('generator_ddim_timesteps', 50),
            eta=input.get('generator_ddim_eta', 0.0))

        # upsampling (256->1024)
        img = F.interpolate(
            img, scale_factor=4.0, mode='bilinear', align_corners=False)
        img = self.diffusion_upsampler_1024.ddim_sample_loop(
            noise=torch.randn_like(img),
            model=self.unet_upsampler_1024,
            model_kwargs={'concat': img},
            percentile=input.get('upsampler_1024_percentile', 0.995),
            ddim_timesteps=input.get('upsampler_1024_ddim_timesteps', 20),
            eta=input.get('upsampler_1024_ddim_eta', 0.0))

        # output
        img = img.clamp(-1, 1).add(1).mul(127.5).squeeze(0).permute(
            1, 2, 0).cpu().numpy().astype(np.uint8)
        return img
