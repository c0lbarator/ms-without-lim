# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .stable_diffusion import StableDiffusionWrapperPipeline
    from .stable_diffusion import ChineseStableDiffusionPipeline
