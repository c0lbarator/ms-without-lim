# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .data_loader import DataLoader
    from .dialog_intent_prediction_preprocessor import \
        DialogIntentPredictionPreprocessor
    from .dialog_modeling_preprocessor import DialogModelingPreprocessor
    from .dialog_state_tracking_preprocessor import DialogStateTrackingPreprocessor
    from .dst_processors import InputFeatures
    from .fields import MultiWOZBPETextField, IntentBPETextField

