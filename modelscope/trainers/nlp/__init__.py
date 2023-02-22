# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .sequence_classification_trainer import SequenceClassificationTrainer
    from .csanmt_translation_trainer import CsanmtTranslationTrainer
    from .text_ranking_trainer import TextRankingTrainer
    from .text_generation_trainer import TextGenerationTrainer
    from .sentence_embedding_trainer import SentenceEmbeddingTrainer
