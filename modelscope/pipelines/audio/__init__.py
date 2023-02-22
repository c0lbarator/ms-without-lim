# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .ans_pipeline import ANSPipeline
    from .asr_inference_pipeline import AutomaticSpeechRecognitionPipeline
    from .kws_farfield_pipeline import KWSFarfieldPipeline
    from .kws_kwsbp_pipeline import KeyWordSpottingKwsbpPipeline
    from .linear_aec_pipeline import LinearAECPipeline
    from .text_to_speech_pipeline import TextToSpeechSambertHifiganPipeline
    from .inverse_text_processing_pipeline import InverseTextProcessingPipeline
    from .speaker_verification_pipeline import SpeakerVerificationPipeline
