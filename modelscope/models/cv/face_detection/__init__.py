# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .mogface import MogFaceDetector
    from .mtcnn import MtcnnFaceDetector
    from .retinaface import RetinaFaceDetection
    from .ulfd_slim import UlfdFaceDetector
    from .scrfd import ScrfdDetect
    from .scrfd import TinyMogDetect
    from .scrfd import SCRFDPreprocessor
