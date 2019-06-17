from django.test import TestCase
from ..models import Sentiments


class PageViewTest(TestCase):

    def test_get_page_should_return_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
 
    def test_should_call_index_temp(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'words/index.html')

    def test_should_show_tag_name(self):
        response = self.client.get('/')
        self.assertContains(response,'hello')

