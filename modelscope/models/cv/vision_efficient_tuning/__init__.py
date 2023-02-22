# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:

    from .vision_efficient_tuning_adapter import VisionEfficientTuningAdapterModel
    from .vision_efficient_tuning_prompt import VisionEfficientTuningPromptModel
    from .vision_efficient_tuning_prefix import VisionEfficientTuningPrefixModel
    from .vision_efficient_tuning_lora import VisionEfficientTuningLoRAModel

