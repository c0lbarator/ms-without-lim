# Modified by Zhipu.AI
# Original Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING, Union

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .codegeex_for_code_translation import CodeGeeXForCodeTranslation
    from .codegeex_for_code_generation import CodeGeeXForCodeGeneration
