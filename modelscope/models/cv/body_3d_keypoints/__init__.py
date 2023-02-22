# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .cannonical_pose import BodyKeypointsDetection3D
    from .hdformer import HDFormerDetector
