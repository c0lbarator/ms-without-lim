# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .text_classification_head import TextClassificationHead
    from .torch_pretrain_head import BertMLMHead, RobertaMLMHead
