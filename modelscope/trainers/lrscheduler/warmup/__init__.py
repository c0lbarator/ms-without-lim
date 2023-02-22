# Copyright (c) Alibaba, Inc. and its affiliates.

from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .base import BaseWarmup
    from .warmup import ConstantWarmup, ExponentialWarmup, LinearWarmup

