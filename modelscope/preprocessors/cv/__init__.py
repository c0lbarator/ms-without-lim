# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .video_super_resolution import (VideoReader)
    from .video_stabilization import (stabilization_preprocessor)
    from .mmcls_preprocessor import ImageClassificationMmcvPreprocessor

    from .image_quality_assessment_mos import ImageQualityAssessmentMosPreprocessor
    from .image_restoration_preprocessor import ImageRestorationPreprocessor
    from .bad_image_detecting_preprocessor import BadImageDetectingPreprocessor

