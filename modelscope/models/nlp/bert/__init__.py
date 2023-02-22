# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .backbone import (
        BertLayer,
        BertModel,
        BertPreTrainedModel,
    )
    from .configuration import BertConfig
    from .fill_mask import BertForMaskedLM
    from .text_ranking import BertForTextRanking
    from .sentence_embedding import BertForSentenceEmbedding
    from .text_classification import BertForSequenceClassification
    from .token_classification import BertForTokenClassification
    from .document_segmentation import BertForDocumentSegmentation
    from .siamese_uie import SiameseUieModel
    from .word_alignment import MBertForWordAlignment
