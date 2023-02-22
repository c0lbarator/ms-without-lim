# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .basic_utils import set_seed, get_state_dict, load_data, init_transform_dict, load_frames_from_video
    from .model import VoP
    from .tokenization_clip import LengthAdaptiveTokenizer
