# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""utils for creating datasets"""
import math
import os
import random
import time

import torch

from . import corpora
from .datasets import (BertSentencepairDataset, BlockDataset, ConcatDataset,
                       GPT2Dataset, ShuffleDataset, SplitDataset, XLDataset,
                       split_ds)
from .lazy_loader import (LazyLoader, LazyWriter, exists_lazy, exists_scatter,
                          get_scatter_path)
from .samplers import DistributedBatchSampler
from .tokenization import (BertWordPieceTokenizer, CharacterLevelTokenizer,
                           CommandToken, GPT2BPETokenizer, Tokenization,
                           Tokenizer, make_tokenizer)

TRAIN_DATA = 0
VAL_DATA = 1
TEST_DATA = 2


def should_split(split):
    """
    given split proportions checks if should split
    Examples:
        >>> should_split([10,0,0])
        >>> False
        >>> should_split([1,.1,.2])
        >>> True
    """
    return max(split) / sum(split) != 1.


def get_ext(path):
    """gets path extension"""
    return os.path.splitext(path)[1]


def get_dataset(name,
                tokenizer,
                pre_tokenize,
                data_parallel_rank,
                loader_scatter=None,
                no_lazy_loader=False,
                half_lazy_loader=False):
    """gets dataset object based on keyword args and file at `path`"""
    global_rank = torch.distributed.get_rank()
    if not supported_corpus(name):
        raise NotImplementedError('dataset %s is not supported' % name)
    dataset = corpora.NAMED_CORPORA[name]
    path = dataset.PATH
    if issubclass(dataset, corpora.PromptReader):
        if not (exists_lazy(path, data_type='prompt')
                and exists_lazy(path, data_type='text')) and not (
                    loader_scatter is not None and exists_scatter(
                        path, data_type='prompt', scatter_num=loader_scatter)
                    and exists_scatter(
                        path, data_type='text', scatter_num=loader_scatter)):
            # create cached version of dataset for lazy loading if it doesn't exist
            if global_rank == 0:
                print(f'Creating lazy loader for dataset {name}')
                prompt_writer = LazyWriter(
                    path, data_type='prompt', is_array=pre_tokenize)
                text_writer = LazyWriter(
                    path, data_type='text', is_array=pre_tokenize)
                writers = {'prompt': prompt_writer, 'text': text_writer}
                reader = dataset(
                    writers=writers,
                    tokenizer=tokenizer,
                    tokenize=pre_tokenize)
                reader.process()
                prompt_writer.close()
                text_writer.close()
