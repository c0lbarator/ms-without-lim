# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .bart import BartForTextErrorCorrection
    from .bert import (
        BertForMaskedLM,
        BertForTextRanking,
        BertForSentenceEmbedding,
        BertForSequenceClassification,
        BertForTokenClassification,
        BertForDocumentSegmentation,
        BertModel,
        BertConfig,
        SiameseUieModel,
    )
    from .bloom import BloomModel
    from .codegeex import CodeGeeXForCodeTranslation, CodeGeeXForCodeGeneration
    from .csanmt import CsanmtForTranslation
    from .deberta_v2 import DebertaV2ForMaskedLM, DebertaV2Model
    from .gpt_neo import GPTNeoModel
    from .gpt2 import GPT2Model
    from .gpt3 import GPT3ForTextGeneration, DistributedGPT3
    from .gpt_moe import GPTMoEForTextGeneration, DistributedGPTMoE
    from .heads import TextClassificationHead
    from .hf_transformers import TransformersModel
    from .lstm import (
        LSTMModel,
        LSTMForTokenClassificationWithCRF,
    )
    from .megatron_bert import (
        MegatronBertConfig,
        MegatronBertForMaskedLM,
        MegatronBertModel,
    )
    from .mglm import MGLMForTextSummarization
    from .palm_v2 import PalmForTextGeneration
    from .plug_mental import (PlugMentalConfig, PlugMentalModel,
                              PlugMentalForSequenceClassification)
    from .ponet import PoNetForMaskedLM, PoNetModel, PoNetConfig
    from .space import SpaceForDialogIntent, SpaceForDialogModeling, SpaceForDST
    from .space_T_cn import TableQuestionAnswering
    from .space_T_en import StarForTextToSql
    from .structbert import (
        SbertForFaqQuestionAnswering,
        SbertForMaskedLM,
        SbertForSequenceClassification,
        SbertForTokenClassification,
        SbertModel,
    )
    from .T5 import T5ForConditionalGeneration
    from .task_models import (
        ModelForFeatureExtraction,
        ModelForInformationExtraction,
        ModelForTextClassification,
        SingleBackboneTaskModelBase,
        ModelForTextGeneration,
        ModelForTextRanking,
        ModelForTokenClassification,
        ModelForTokenClassificationWithCRF,
    )
    from .unite import UniTEForTranslationEvaluation
    from .use import UserSatisfactionEstimation
    from .veco import (VecoConfig, VecoForMaskedLM,
                       VecoForSequenceClassification,
                       VecoForTokenClassification, VecoModel)
    from .dgds import (DocumentGroundedDialogGenerateModel,
                       DocumentGroundedDialogRetrievalModel,
                       DocumentGroundedDialogRerankModel)
    from .xlm_roberta import XLMRobertaConfig, XLMRobertaModel

