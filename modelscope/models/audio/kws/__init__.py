# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .generic_key_word_spotting import GenericKeyWordSpotting
    from .farfield.model import FSMNSeleNetV2Decorator
    from .nearfield.model import FSMNDecorator

