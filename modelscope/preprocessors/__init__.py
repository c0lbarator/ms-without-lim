# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .base import Preprocessor
    from .builder import PREPROCESSORS, build_preprocessor
    from .common import Compose, ToTensor, Filter
    from .asr import WavToScp
    from .audio import LinearAECAndFbank, AudioBrainPreprocessor
    from .image import (LoadImage, load_image,
                        ImageColorEnhanceFinetunePreprocessor,
                        ImageInstanceSegmentationPreprocessor,
                        ImageDenoisePreprocessor, ImageDeblurPreprocessor)
    from .cv import (ImageClassificationMmcvPreprocessor,
                     ImageRestorationPreprocessor)
    from .kws import WavToLists
    from .tts import KanttsDataPreprocessor
    from .multi_modal import (OfaPreprocessor, MPlugPreprocessor,
                              HiTeAPreprocessor)
    from .nlp import (
        DocumentSegmentationTransformersPreprocessor,
        FaqQuestionAnsweringTransformersPreprocessor,
        FillMaskPoNetPreprocessor, FillMaskTransformersPreprocessor,
        TextRankingTransformersPreprocessor,
        RelationExtractionTransformersPreprocessor,
        SentenceEmbeddingTransformersPreprocessor,
        TextClassificationTransformersPreprocessor,
        TextGenerationSentencePiecePreprocessor,
        TokenClassificationTransformersPreprocessor,
        TextErrorCorrectionPreprocessor, TextGenerationT5Preprocessor,
        WordAlignmentPreprocessor, TextGenerationTransformersPreprocessor,
        Tokenize, WordSegmentationBlankSetToLabelPreprocessor,
        CodeGeeXPreprocessor, MGLMSummarizationPreprocessor,
        ZeroShotClassificationTransformersPreprocessor,
        TextGenerationJiebaPreprocessor, SentencePiecePreprocessor,
        DialogIntentPredictionPreprocessor, DialogModelingPreprocessor,
        DialogStateTrackingPreprocessor, ConversationalTextToSqlPreprocessor,
        TableQuestionAnsweringPreprocessor, NERPreprocessorViet,
        NERPreprocessorThai, WordSegmentationPreprocessorThai,
        TranslationEvaluationPreprocessor,
        DialogueClassificationUsePreprocessor, SiameseUiePreprocessor,
        DocumentGroundedDialogGeneratePreprocessor,
        DocumentGroundedDialogRetrievalPreprocessor,
        DocumentGroundedDialogRerankPreprocessor)
    from .video import ReadVideoData, MovieSceneSegmentationPreprocessor

