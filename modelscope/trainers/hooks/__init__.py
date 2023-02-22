# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .builder import HOOKS, build_hook
    from .checkpoint_hook import BestCkptSaverHook, CheckpointHook, LoadCheckpointHook
    from .early_stop_hook import EarlyStopHook
    from .compression import SparsityHook
    from .evaluation_hook import EvaluationHook
    from .hook import Hook
    from .iter_timer_hook import IterTimerHook
    from .logger import TensorboardHook, TextLoggerHook
    from .lr_scheduler_hook import LrSchedulerHook
    from .optimizer import (ApexAMPOptimizerHook, NoneOptimizerHook,
                            OptimizerHook, TorchAMPOptimizerHook)
    from .priority import Priority, get_priority

