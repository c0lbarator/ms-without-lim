# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .builder import LR_SCHEDULER, build_lr_scheduler
    from .warmup import BaseWarmup, ConstantWarmup, ExponentialWarmup, LinearWarmup

