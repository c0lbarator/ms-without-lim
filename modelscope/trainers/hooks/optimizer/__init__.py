# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .apex_optimizer_hook import ApexAMPOptimizerHook
    from .base import OptimizerHook, NoneOptimizerHook
    from .torch_optimizer_hook import TorchAMPOptimizerHook

