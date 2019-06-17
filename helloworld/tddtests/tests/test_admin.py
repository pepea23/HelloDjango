from django.test import TestCase
from ..admin import SentimentsAdmin


class AdminTest(TestCase):
    def test_checkwords_urls_admin_should_have_302(self):
        expected = 302
        self.assertEqual(self.client.get('/admin/tddtests/sentiments/').status_code, expected)

    def test_checkwords_should_have_list_display(self):
        expected = [
            'word',
            'goodbad'
        ]
        self.assertEqual(SentimentsAdmin.list_display, expected)


    def test_checkwords_should_have_list_filter(self):
        expected = [
            'date',
        ]
        self.assertEqual(SentimentsAdmin.list_filter, expected)

    def test_checkwords_should_have_search_fields(self):
        expected = [
            'word',
        ]
        self.assertEqual(SentimentsAdmin.search_fields, expected)
