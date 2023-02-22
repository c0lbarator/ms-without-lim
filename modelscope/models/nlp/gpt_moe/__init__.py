# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .configuration import GPTMoEConfig
    from .backbone import GPTMoEModel
    from .text_generation import GPTMoEForTextGeneration
    from .tokenizer import JiebaBPETokenizer
    from .distributed_gpt_moe import DistributedGPTMoE
