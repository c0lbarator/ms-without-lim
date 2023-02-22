# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .sparsity_hook import SparsityHook
    from .utils import SparseLinear, convert_sparse_network

