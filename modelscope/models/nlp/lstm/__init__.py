# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .backbone import LSTMModel
    from .token_classification import LSTMForTokenClassificationWithCRF
