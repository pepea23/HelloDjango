from django.test import TestCase
from .models import Sentiments
from django.db.models import CharField
from django.db.models import IntegerField


class SentimentsModelTest(TestCase):
    def test_should_have_wrods_field(self):
        sentiments = Sentiments._meta.get_field('word')
        self.assertTrue(isinstance(sentiments, CharField))

    def test_should_have_goodbad_field(self):
        goodbad = Sentiments._meta.get_field('goodbad')
        self.assertTrue(isinstance(goodbad, IntegerField))

    def test_create_field(self):
        sentiments=Sentiments.objects.create(word = "hi", goodbad = 1)
        self.assertEqual(sentiments.word,'hi')
        self.assertEqual(sentiments.goodbad,1)
