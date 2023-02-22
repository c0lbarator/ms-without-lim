# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .detection_pipeline import EasyCVDetectionPipeline
    from .segmentation_pipeline import EasyCVSegmentationPipeline
    from .face_2d_keypoints_pipeline import Face2DKeypointsPipeline
    from .human_wholebody_keypoint_pipeline import HumanWholebodyKeypointsPipeline
