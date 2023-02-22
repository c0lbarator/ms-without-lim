# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .document_grounded_dialog_generate import DocumentGroundedDialogGenerateModel
    from .document_grounded_dialog_retrieval import DocumentGroundedDialogRerankModel
    from .document_grounded_dialog_retrieval import DocumentGroundedDialogRetrievalModel
