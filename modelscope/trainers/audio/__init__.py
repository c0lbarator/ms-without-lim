# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    print('True...')
    from .tts_trainer import KanttsTrainer
    from .ans_trainer import ANSTrainer
    from .kws_nearfield_trainer import KWSNearfieldTrainer
    from .kws_farfield_trainer import KWSFarfieldTrainer

