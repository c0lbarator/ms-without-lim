# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:

    from .clip import CLIPForMultiModalEmbedding
    from .gemm import GEMMForMultiModalEmbedding
    from .team import TEAMForMultiModalSimilarity
    from .diffusion import DiffusionForTextToImageSynthesis
    from .mmr import VideoCLIPForMultiModalEmbedding
    from .mplug_for_all_tasks import MPlugForAllTasks, HiTeAForAllTasks
    from .ofa_for_all_tasks import OfaForAllTasks
    from .ofa_for_text_to_image_synthesis_model import \
        OfaForTextToImageSynthesis
    from .multi_stage_diffusion import \
        MultiStageDiffusionForTextToImageSynthesis
    from .vldoc import VLDocForDocVLEmbedding

