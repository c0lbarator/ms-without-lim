# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .facelib.facer import FaceAna
    from .mtcnn_pytorch.src.align_trans import (get_reference_facial_points,
                                                warp_and_crop_face)
    from .utils import (get_f5p, padTo16x, resize_size)

