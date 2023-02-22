# Copyright (c) Alibaba, Inc. and its affiliates.
# The DAMO-YOLO implementation is also open-sourced by the authors at https://github.com/tinyvision/damo-yolo.

from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .tinynas_detector import Tinynas_detector
    from .tinynas_damoyolo import DamoYolo

