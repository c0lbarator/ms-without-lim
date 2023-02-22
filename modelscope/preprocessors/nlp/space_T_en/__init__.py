# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .conversational_text_to_sql_preprocessor import \
        ConversationalTextToSqlPreprocessor
    from .fields import (get_label, SubPreprocessor, preprocess_dataset,
                         process_dataset)

