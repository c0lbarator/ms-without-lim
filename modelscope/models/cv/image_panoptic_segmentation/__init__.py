# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .panseg_model import SwinLPanopticSegmentation
    from .r50_panseg_model import R50PanopticSegmentation

