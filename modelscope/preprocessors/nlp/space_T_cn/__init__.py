# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .table_question_answering_preprocessor import TableQuestionAnsweringPreprocessor
    from .fields import MultiWOZBPETextField, IntentBPETextField

