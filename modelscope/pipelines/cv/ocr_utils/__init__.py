# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .model_resnet_mutex_v4_linewithchar import SegLinkDetector
    from .ops import decode_segments_links_python, combine_segments_python
    from .utils import (rboxes_to_polygons, cal_width, nms_python,
                        polygons_from_bitmap, rboxes_from_bitmap)
