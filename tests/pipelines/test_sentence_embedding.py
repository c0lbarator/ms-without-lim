# Copyright (c) Alibaba, Inc. and its affiliates.
import shutil
import unittest

from modelscope.hub.snapshot_download import snapshot_download
from modelscope.models import Model
from modelscope.models.nlp import BertForSentenceEmbedding
from modelscope.pipelines import pipeline
from modelscope.pipelines.nlp import SentenceEmbeddingPipeline
from modelscope.preprocessors import SentenceEmbeddingTransformersPreprocessor
from modelscope.utils.constant import Tasks
from modelscope.utils.test_utils import test_level


class SentenceEmbeddingTest(unittest.TestCase):
    model_id = 'damo/nlp_corom_sentence-embedding_english-base'
    tiny_model_id = 'damo/nlp_corom_sentence-embedding_english-tiny'
    ecom_base_model_id = 'damo/nlp_corom_sentence-embedding_chinese-base-ecom'
    ecom_tiny_model_id = 'damo/nlp_corom_sentence-embedding_chinese-tiny-ecom'
    medical_base_model_id = 'damo/nlp_corom_sentence-embedding_chinese-base-medical'
    medical_tiny_model_id = 'damo/nlp_corom_sentence-embedding_chinese-tiny-medical'
    general_base_model_id = 'damo/nlp_corom_sentence-embedding_chinese-base'
    general_tiny_model_id = 'damo/nlp_corom_sentence-embedding_chinese-tiny'

    inputs = {
        'source_sentence': ["how long it take to get a master's degree"],
        'sentences_to_compare': [
            "On average, students take about 18 to 24 months to complete a master's degree.",
            'On the other hand, some students prefer to go at a slower pace and choose to take ',
            'several years to complete their studies.',
            'It can take anywhere from two semesters'
        ]
    }

    inputs2 = {
        'source_sentence': ["how long it take to get a master's degree"],
        'sentences_to_compare': [
            "On average, students take about 18 to 24 months to complete a master's degree."
        ]
    }

    inputs3 = {
        'source_sentence': ["how long it take to get a master's degree"],
        'sentences_to_compare': []
    }

    inputs4 = {
        'source_sentence': ["how long it take to get a master's degree"]
    }

    inputs5 = {
        'source_sentence': [
            'how long it take to get a master degree',
            'students take about 18 to 24 months to complete a degree'
        ]
    }

    general_inputs1 = {
        'source_sentence': ['?????????????????????'],
        'sentences_to_compare': [
            '???????????????????????????????????????????????????',
            '???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????,??????>????????????,??????????????????????????????????????????;?????????????????????,????????????????????????',
            '???????????????????????????,??????????????????????????????????????????????????????P??????,????????????????????????Watt???,????????????Wa????????????W.???????????????????????????????????????????????? ???????????????,???????????????\
             ,????????????.???????????????????????????????????????????????????,?????????????????????????????????????????????!',
        ]
    }

    general_inputs2 = {
        'source_sentence': [
            '???????????????????????????????????????????????????',
            '???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????,??????>????????????,??????????????????????????????????????????;?????????????????????,????????????????????????',
            '???????????????????????????,??????????????????????????????????????????????????????P??????,????????????????????????Watt???,????????????Wa????????????W.???????????????????????????????????????????????? ???????????????,???????????????\
             ,????????????.???????????????????????????????????????????????????,?????????????????????????????????????????????!',
        ]
    }

    ecom_inputs1 = {
        'source_sentence': ['????????????'],
        'sentences_to_compare': ['??????????????????????????????????????????????????????', '????????????????????????']
    }

    ecom_inputs2 = {'source_sentence': ['????????????', '?????????????????????']}

    medical_inputs1 = {
        'source_sentence': ['????????????????????????????????????'],
        'sentences_to_compare': ['???????????????????????????,??????????????????????????????????????????', '???????????????????????????']
    }

    medical_inputs2 = {'source_sentence': ['????????????????????????????????????', '????????????????????????????????????']}

    el_model_id = 'damo/nlp_bert_entity-embedding_chinese-base'
    el_inputs = {
        'source_sentence': ['????????????????????????????????? [ENT_S] ?????? [ENT_E] ????????????????????????????????????????????????'],
        'sentences_to_compare': [
            '???????????? ????????? Person??? ????????? Da Peng??? ??????;',
            '??????????????? ????????? Work??? ????????? ????????? ??????!??????????????? Super Wings;',
            '????????? ????????? Person??? ????????? Roy;',
        ]
    }

    @unittest.skipUnless(test_level() >= 2, 'skip test in current test level')
    def test_run_by_direct_model_download(self):
        cache_path = snapshot_download(self.model_id)
        tokenizer = SentenceEmbeddingTransformersPreprocessor(cache_path)
        model = BertForSentenceEmbedding.from_pretrained(cache_path)
        pipeline1 = SentenceEmbeddingPipeline(model, preprocessor=tokenizer)
        pipeline2 = pipeline(
            Tasks.sentence_embedding, model=model, preprocessor=tokenizer)
        print(f'inputs: {self.inputs}\n'
              f'pipeline1:{pipeline1(input=self.inputs)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.inputs)}')
        print()
        print(f'inputs: {self.inputs2}\n'
              f'pipeline1:{pipeline1(input=self.inputs2)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.inputs2)}')
        print(f'inputs: {self.inputs3}\n'
              f'pipeline1:{pipeline1(input=self.inputs3)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.inputs3)}')
        print(f'inputs: {self.inputs4}\n'
              f'pipeline1:{pipeline1(input=self.inputs4)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.inputs4)}')
        print(f'inputs: {self.inputs5}\n'
              f'pipeline1:{pipeline1(input=self.inputs5)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.inputs5)}')

    @unittest.skipUnless(test_level() >= 2, 'skip test in current test level')
    def test_ecom_model_run_by_direct_model_download(self):
        cache_path = snapshot_download(self.ecom_base_model_id)
        tokenizer = SentenceEmbeddingTransformersPreprocessor(cache_path)
        model = BertForSentenceEmbedding.from_pretrained(cache_path)
        pipeline1 = SentenceEmbeddingPipeline(model, preprocessor=tokenizer)
        pipeline2 = pipeline(
            Tasks.sentence_embedding, model=model, preprocessor=tokenizer)
        print(f'inputs: {self.ecom_inputs1}\n'
              f'pipeline1:{pipeline1(input=self.ecom_inputs1)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.ecom_inputs1)}')

    @unittest.skipUnless(test_level() >= 2, 'skip test in current test level')
    def test_medical_model_run_by_direct_model_download(self):
        cache_path = snapshot_download(self.medical_base_model_id)
        tokenizer = SentenceEmbeddingTransformersPreprocessor(cache_path)
        model = BertForSentenceEmbedding.from_pretrained(cache_path)
        pipeline1 = SentenceEmbeddingPipeline(model, preprocessor=tokenizer)
        pipeline2 = pipeline(
            Tasks.sentence_embedding, model=model, preprocessor=tokenizer)
        print(f'inputs: {self.medical_inputs1}\n'
              f'pipeline1:{pipeline1(input=self.medical_inputs1)}')
        print()
        print(f'pipeline2: {pipeline2(input=self.medical_inputs1)}')

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_run_with_model_from_modelhub(self):
        model = Model.from_pretrained(self.model_id)
        tokenizer = SentenceEmbeddingTransformersPreprocessor(model.model_dir)
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=model, preprocessor=tokenizer)
        print(pipeline_ins(input=self.inputs))

    @unittest.skipUnless(test_level() >= 1, 'skip test in current test level')
    def test_run_with_model_name(self):
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.model_id)
        print(pipeline_ins(input=self.inputs))
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.tiny_model_id)
        print(pipeline_ins(input=self.inputs))

    @unittest.skipUnless(test_level() >= 2, 'skip test in current test level')
    def test_run_with_default_model(self):
        pipeline_ins = pipeline(task=Tasks.sentence_embedding)
        print(pipeline_ins(input=self.inputs))

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_run_ecom_model_with_model_name(self):
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.ecom_base_model_id)
        print(pipeline_ins(input=self.ecom_inputs2))
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.ecom_tiny_model_id)
        print(pipeline_ins(input=self.ecom_inputs2))

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_run_medical_model_with_model_name(self):
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.medical_base_model_id)
        print(pipeline_ins(input=self.medical_inputs1))
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.medical_tiny_model_id)
        print(pipeline_ins(input=self.medical_inputs1))

    @unittest.skipUnless(test_level() >= 2, 'skip test in current test level')
    def test_run_with_el_model(self):
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.el_model_id)
        print(pipeline_ins(input=self.el_inputs))

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_run_general_model_with_model_name(self):
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.general_base_model_id)
        print(pipeline_ins(input=self.general_inputs1))
        print(pipeline_ins(input=self.general_inputs2))
        pipeline_ins = pipeline(
            task=Tasks.sentence_embedding, model=self.general_tiny_model_id)
        print(pipeline_ins(input=self.general_inputs1))
        print(pipeline_ins(input=self.general_inputs2))


if __name__ == '__main__':
    unittest.main()
