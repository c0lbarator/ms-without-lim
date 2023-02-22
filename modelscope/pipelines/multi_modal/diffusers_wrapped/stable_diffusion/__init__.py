# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .stable_diffusion_pipeline import StableDiffusionWrapperPipeline
    from .chinese_stable_diffusion_pipeline import ChineseStableDiffusionPipeline
