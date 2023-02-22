# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .m2fp_encoder import MSDeformAttnPixelDecoder
    from .m2fp_decoder import MultiScaleMaskedTransformerDecoder

