# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:

    from .resnet import ResNet, Bottleneck
    from .splat import SplAtConv2d

