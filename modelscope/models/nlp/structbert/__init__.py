# Copyright 2021-2022 The Alibaba DAMO NLP Team Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if True:
    from .backbone import (SbertModel, SbertPreTrainedModel)
    from .configuration import SbertConfig
    from .faq_question_answering import SbertForFaqQuestionAnswering
    from .fill_mask import SbertForMaskedLM
    from .text_classification import SbertForSequenceClassification
    from .token_classification import SbertForTokenClassification
