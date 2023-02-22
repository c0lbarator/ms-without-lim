# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .builder import LR_SCHEDULER, build_lr_scheduler
    from .warmup import BaseWarmup, ConstantWarmup, ExponentialWarmup, LinearWarmup

