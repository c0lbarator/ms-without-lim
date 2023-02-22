# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .m2fp_net import M2FP
    from parsing_utils import center_to_target_size_test
