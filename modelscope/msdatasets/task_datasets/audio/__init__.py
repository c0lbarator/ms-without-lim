# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .kws_farfield_dataset import KWSDataset, KWSDataLoader
    from .kws_nearfield_dataset import kws_nearfield_dataset

