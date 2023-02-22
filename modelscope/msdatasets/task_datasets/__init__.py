# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule, is_torch_available

if True:
    from .base import TaskDataset
    from .builder import TASK_DATASETS, build_task_dataset
    from .torch_base_dataset import TorchTaskDataset
    from .veco_dataset import VecoDataset
    from .image_instance_segmentation_coco_dataset import ImageInstanceSegmentationCocoDataset
    from .movie_scene_segmentation import MovieSceneSegmentationDataset
    from .video_summarization_dataset import VideoSummarizationDataset
    from .language_guided_video_summarization_dataset import LanguageGuidedVideoSummarizationDataset
    from .image_inpainting import ImageInpaintingDataset
    from .text_ranking_dataset import TextRankingDataset
    from .referring_video_object_segmentation import ReferringVideoObjectSegmentationDataset
    from .bad_image_detecting import BadImageDetectingDataset

