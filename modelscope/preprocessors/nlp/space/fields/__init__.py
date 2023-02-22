# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .gen_field import MultiWOZBPETextField
    from .intent_field import IntentBPETextField
