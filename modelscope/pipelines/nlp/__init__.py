# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .automatic_post_editing_pipeline import AutomaticPostEditingPipeline
    from .conversational_text_to_sql_pipeline import ConversationalTextToSqlPipeline
    from .table_question_answering_pipeline import TableQuestionAnsweringPipeline
    from .dialog_intent_prediction_pipeline import DialogIntentPredictionPipeline
    from .dialog_modeling_pipeline import DialogModelingPipeline
    from .dialog_state_tracking_pipeline import DialogStateTrackingPipeline
    from .document_segmentation_pipeline import DocumentSegmentationPipeline
    from .extractive_summarization_pipeline import ExtractiveSummarizationPipeline
    from .fasttext_text_classification_pipeline import FasttextSequenceClassificationPipeline
    from .faq_question_answering_pipeline import FaqQuestionAnsweringPipeline
    from .feature_extraction_pipeline import FeatureExtractionPipeline
    from .fill_mask_pipeline import FillMaskPipeline
    from .information_extraction_pipeline import InformationExtractionPipeline
    from .interactive_translation_pipeline import InteractiveTranslationPipeline
    from .named_entity_recognition_pipeline import NamedEntityRecognitionPipeline
    from .text_ranking_pipeline import TextRankingPipeline
    from .sentence_embedding_pipeline import SentenceEmbeddingPipeline
    from .text_classification_pipeline import TextClassificationPipeline
    from .summarization_pipeline import SummarizationPipeline
    from .translation_quality_estimation_pipeline import TranslationQualityEstimationPipeline
    from .text_error_correction_pipeline import TextErrorCorrectionPipeline
    from .word_alignment_pipeline import WordAlignmentPipeline
    from .text_generation_pipeline import TextGenerationPipeline, TextGenerationT5Pipeline
    from .fid_dialogue_pipeline import FidDialoguePipeline
    from .token_classification_pipeline import TokenClassificationPipeline
    from .translation_pipeline import TranslationPipeline
    from .word_segmentation_pipeline import WordSegmentationPipeline, WordSegmentationThaiPipeline
    from .zero_shot_classification_pipeline import ZeroShotClassificationPipeline
    from .mglm_text_summarization_pipeline import MGLMTextSummarizationPipeline
    from .codegeex_code_translation_pipeline import CodeGeeXCodeTranslationPipeline
    from .codegeex_code_generation_pipeline import CodeGeeXCodeGenerationPipeline
    from .translation_evaluation_pipeline import TranslationEvaluationPipeline
    from .user_satisfaction_estimation_pipeline import UserSatisfactionEstimationPipeline
    from .siamese_uie_pipeline import SiameseUiePipeline
    from .document_grounded_dialog_generate_pipeline import DocumentGroundedDialogGeneratePipeline
    from .document_grounded_dialog_retrieval_pipeline import DocumentGroundedDialogRetrievalPipeline
    from .document_grounded_dialog_rerank_pipeline import DocumentGroundedDialogRerankPipeline

