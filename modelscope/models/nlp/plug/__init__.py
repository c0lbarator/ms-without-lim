# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .configuration import PlugNLGConfig
    from .backbone import PlugModel
    from .distributed_plug import DistributedPlug
