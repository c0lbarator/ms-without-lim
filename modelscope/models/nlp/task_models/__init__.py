# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .information_extraction import ModelForInformationExtraction
    from .feature_extraction import ModelForFeatureExtraction
    from .fill_mask import ModelForFillMask
    from .text_classification import ModelForTextClassification
    from .task_model import SingleBackboneTaskModelBase
    from .token_classification import (ModelForTokenClassification,
                                       ModelForTokenClassificationWithCRF)
    from .text_generation import ModelForTextGeneration
    from .text_ranking import ModelForTextRanking

