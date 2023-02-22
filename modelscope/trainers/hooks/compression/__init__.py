# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .sparsity_hook import SparsityHook
    from .utils import SparseLinear, convert_sparse_network

