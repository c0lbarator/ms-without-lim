# Copyright (c) Alibaba, Inc. and its affiliates.

import torch
from torch.nn.parallel import DistributedDataParallel

import modelscope.models.audio.tts.kantts.train.scheduler as kantts_scheduler
from modelscope.models.audio.tts.kantts.utils.ling_unit.ling_unit import \
    get_fpdict
from .hifigan import (Generator, MultiPeriodDiscriminator,
                      MultiScaleDiscriminator, MultiSpecDiscriminator)
from .pqmf import PQMF
from .sambert.kantts_sambert import KanTtsSAMBERT, KanTtsTextsyBERT


def optimizer_builder(model_params, opt_name, opt_params):
    opt_cls = getattr(torch.optim, opt_name)
    optimizer = opt_cls(model_params, **opt_params)
    return optimizer


def scheduler_builder(optimizer, sche_name, sche_params):
    scheduler_cls = getattr(kantts_scheduler, sche_name)
    scheduler = scheduler_cls(optimizer, **sche_params)
    return scheduler


def hifigan_model_builder(config, device, rank, distributed):
    model = {}
    optimizer = {}
    scheduler = {}
    model['discriminator'] = {}
    optimizer['discriminator'] = {}
    scheduler['discriminator'] = {}
    for model_name in config['Model'].keys():
        if model_name == 'Generator':
            params = config['Model'][model_name]['params']
            model['generator'] = Generator(**params).to(device)
            optimizer['generator'] = optimizer_builder(
                model['generator'].parameters(),
                config['Model'][model_name]['optimizer'].get('type', 'Adam'),
                config['Model'][model_name]['optimizer'].get('params', {}),
            )
            scheduler['generator'] = scheduler_builder(
                optimizer['generator'],
                config['Model'][model_name]['scheduler'].get('type', 'StepLR'),
                config['Model'][model_name]['scheduler'].get('params', {}),
            )
