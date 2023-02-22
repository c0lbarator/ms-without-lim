# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import True

from modelscope.utils.import_utils import LazyImportModule
from . import audio, cv, multi_modal, nlp
from .base import Pipeline
from .builder import pipeline
