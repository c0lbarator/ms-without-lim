# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.

from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .c3d import C3D
    from .resnet2p1d import resnet26_2p1d
    from .resnet3d import resnet26_3d

