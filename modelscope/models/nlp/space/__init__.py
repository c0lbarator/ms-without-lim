# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .model import SpaceGenerator
    from .model import SpaceModelBase, SpaceTokenizer
    from .dialog_intent_prediction import SpaceForDialogIntent
    from .dialog_modeling import SpaceForDialogModeling
    from .dialog_state_tracking import SpaceForDST
    from .configuration import SpaceConfig
