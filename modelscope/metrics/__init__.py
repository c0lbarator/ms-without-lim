# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .audio_noise_metric import AudioNoiseMetric
    from .base import Metric
    from .builder import METRICS, build_metric, task_default_metrics
    from .image_color_enhance_metric import ImageColorEnhanceMetric
    from .image_denoise_metric import ImageDenoiseMetric
    from .image_instance_segmentation_metric import \
        ImageInstanceSegmentationCOCOMetric
    from .image_portrait_enhancement_metric import ImagePortraitEnhancementMetric
    from .sequence_classification_metric import SequenceClassificationMetric
    from .text_generation_metric import TextGenerationMetric
    from .token_classification_metric import TokenClassificationMetric
    from .video_summarization_metric import VideoSummarizationMetric
    from .movie_scene_segmentation_metric import MovieSceneSegmentationMetric
    from .accuracy_metric import AccuracyMetric
    from .bleu_metric import BleuMetric
    from .image_inpainting_metric import ImageInpaintingMetric
    from .referring_video_object_segmentation_metric import ReferringVideoObjectSegmentationMetric
    from .video_frame_interpolation_metric import VideoFrameInterpolationMetric
    from .video_stabilization_metric import VideoStabilizationMetric
    from .video_super_resolution_metric.video_super_resolution_metric import VideoSuperResolutionMetric
    from .ppl_metric import PplMetric
    from .image_quality_assessment_degradation_metric import ImageQualityAssessmentDegradationMetric
    from .image_quality_assessment_mos_metric import ImageQualityAssessmentMosMetric
    from .text_ranking_metric import TextRankingMetric
    from .loss_metric import LossMetric
