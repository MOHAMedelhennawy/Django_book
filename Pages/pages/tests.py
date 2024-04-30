from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        respons = self.client.get('/')
        self.assertEqual(respons.status_code, 200)
    
    def test_about_page_status_code(self):
        respons = self.client.get('/about/')
        self.assertEqual(respons.status_code, 200)
