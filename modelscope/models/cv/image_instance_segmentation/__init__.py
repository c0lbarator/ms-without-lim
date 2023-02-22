# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .cascade_mask_rcnn_swin import CascadeMaskRCNNSwin
    from .maskdino_swin import MaskDINOSwin
    from .model import CascadeMaskRCNNSwinModel
    from .maskdino_model import MaskDINOSwinModel
    from .postprocess_utils import get_img_ins_seg_result, get_maskdino_ins_seg_result
