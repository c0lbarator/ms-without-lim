# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .configuration import GPT3Config
    from .backbone import GPT3Model
    from .text_generation import GPT3ForTextGeneration
    from .tokenizer import JiebaBPETokenizer
    from .distributed_gpt3 import DistributedGPT3
