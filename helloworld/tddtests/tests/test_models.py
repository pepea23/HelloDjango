from django.test import TestCase
from django.db.models import CharField
from django.db.models import IntegerField

from ..models import Sentiments


class SentimentsModelTest(TestCase):
    def test_should_have_wrods_field(self):
        sentiments = Sentiments._meta.get_field('word')
        self.assertTrue(isinstance(sentiments, CharField))

    def test_should_have_goodbad_field(self):
        goodbad = Sentiments._meta.get_field('goodbad')
        self.assertTrue(isinstance(goodbad, IntegerField))

    def test_create_field_good_words_should_have_word_and_status(self):
        sentiments_1 = Sentiments.objects.create(word = "hi", goodbad = 1)
        sentiments_2 = Sentiments.objects.create(word = "shit", goodbad = -1)
        
        self.assertEqual([sentiments_1.word, sentiments_1.goodbad],['hi',1])
        self.assertEqual([sentiments_2.word, sentiments_2.goodbad],['shit',-1])
