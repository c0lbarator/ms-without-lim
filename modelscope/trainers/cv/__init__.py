# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .image_instance_segmentation_trainer import \
        ImageInstanceSegmentationTrainer
    from .image_portrait_enhancement_trainer import ImagePortraitEnhancementTrainer
    from .movie_scene_segmentation_trainer import MovieSceneSegmentationTrainer
    from .image_inpainting_trainer import ImageInpaintingTrainer
    from .referring_video_object_segmentation_trainer import ReferringVideoObjectSegmentationTrainer
    from .image_defrcn_fewshot_detection_trainer import ImageDefrcnFewshotTrainer

