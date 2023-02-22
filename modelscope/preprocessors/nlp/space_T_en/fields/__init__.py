# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .common_utils import SubPreprocessor
    from .parse import get_label
    from .preprocess_dataset import \
        preprocess_dataset
    from .process_dataset import \
        process_dataset, process_tables

