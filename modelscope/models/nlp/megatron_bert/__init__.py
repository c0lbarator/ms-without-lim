# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .configuration import MegatronBertConfig
    from .backbone import MegatronBertModel
    from .fill_mask import MegatronBertForMaskedLM
