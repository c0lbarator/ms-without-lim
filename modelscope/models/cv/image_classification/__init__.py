# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .mmcls_model import ClassificationModel
    from .resnet50_cc import ContentCheckBackbone

