# Copyright (c) Alibaba, Inc. and its affiliates.

from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .configuration_unite import UniTEConfig
    from .modeling_unite import UniTEForTranslationEvaluation
