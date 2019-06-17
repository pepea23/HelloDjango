from django.test import TestCase
from django.db.models import CharField, IntegerField

from ..models import Sentiments


class SentimentsModelTest(TestCase):
    def test_should_have_words_field(self):
        sentiments = Sentiments._meta.get_field('word')
        self.assertTrue(isinstance(sentiments, CharField))

    def test_should_have_goodbad_field(self):
        is_good_or_is_bad = Sentiments._meta.get_field('goodbad')
        self.assertTrue(isinstance(is_good_or_is_bad, IntegerField))

    def test_create_field_good_bad_words_should_have_word_and_status(self):
        is_good = Sentiments.objects.create(word = "hi", goodbad = 1)
        is_bad = Sentiments.objects.create(word = "shit", goodbad = -1)
        
        self.assertEqual([is_good.word, is_good.goodbad], ['hi', 1])
        self.assertEqual([is_bad.word, is_bad.goodbad], ['shit', -1])
