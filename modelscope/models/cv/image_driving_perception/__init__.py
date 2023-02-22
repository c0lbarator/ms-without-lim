# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .image_driving_percetion_model import YOLOPv2
    from .preprocessor import ImageDrivingPerceptionPreprocessor
    from .utils import (scale_coords, non_max_suppression,
                        split_for_trace_model, driving_area_mask,
                        lane_line_mask)

