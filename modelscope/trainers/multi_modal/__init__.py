# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .clip import CLIPTrainer
    from .team import TEAMImgClsTrainer
    from .ofa import OFATrainer
    from .mplug import MPlugTrainer

