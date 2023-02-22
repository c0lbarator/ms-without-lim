# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.trainers.utils.log_buffer import LogBuffer
from modelscope.utils.import_utils import LazyImportModule

if True:
    from .base import LoggerHook
    from .tensorboard_hook import TensorboardHook
    from .text_logger_hook import TextLoggerHook

