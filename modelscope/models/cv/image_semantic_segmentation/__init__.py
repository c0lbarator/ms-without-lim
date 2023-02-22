# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .semantic_seg_model import SemanticSegmentation
    from .segformer import Segformer
    from .ddpm_segmentation_model import DDPMSegmentationModel

