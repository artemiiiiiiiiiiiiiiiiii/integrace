from django.test import TestCase, Client
from .views import index


class ReplacerTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_page_GET_is_working(self):
        response = self.client.get(path='')
        self.assertEqual(response.status_code, 200)

    def test_index_page_POST_is_working(self):
            response = self.client.post(path='', data={'SendMeText': '"йокарный бабай сказала йошкарала"'})
            self.assertEqual(response.status_code, 200)

    def test_index_page_returned_headers(self):
            response = self.client.post(path='', data={'SendMeText': '"йокарный бабай сказала йошкарала"'})
            self.assertEqual(response.headers.get('Content-Type'), 'text/html; charset=utf-8')

    def test_index_page_changes_brackets(self):
            response = self.client.post(path='', data={'SendMeText': '"йокарный бабай сказала йошкарала"'})
            html_answer = ''.join([r.decode() for r in response])
            self.assertEqual(html_answer, "Текст - \"йокарный бабай сказала йошкарала\"  |   Извлеченные слова - ['иокарный', 'иошкарала']")