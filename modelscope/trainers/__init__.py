# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .audio import ANSTrainer, KanttsTrainer
    from .base import DummyTrainer
    from .builder import build_trainer
    from .cv import (ImageInstanceSegmentationTrainer,
                     ImagePortraitEnhancementTrainer,
                     MovieSceneSegmentationTrainer, ImageInpaintingTrainer,
                     ReferringVideoObjectSegmentationTrainer)
    from .multi_modal import CLIPTrainer
    from .nlp import SequenceClassificationTrainer, TextRankingTrainer
    from .nlp_trainer import NlpEpochBasedTrainer, VecoTrainer
    from .trainer import EpochBasedTrainer

