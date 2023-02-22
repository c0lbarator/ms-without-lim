# Copyright (c) Alibaba, Inc. and its affiliates.

from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .backbone import T5Model
    from .text2text_generation import T5ForConditionalGeneration

