from django.test import TestCase
from ..models import Sentiments


class LandingPageViewTest(TestCase):
    def test_view_should_have_from_with_word_and_type_and_submit_button(self):
        response = self.client.get('/')
        expected = '<form action = "." method ="post">'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type= "text" name="words"'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type = "number" name="type" />'
        self.assertContains(response, expected, status_code=200)
        expected = '<button type = "submit" >Submit </button>'
        self.assertContains(response, expected, status_code=200)

 