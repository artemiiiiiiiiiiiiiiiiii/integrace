from rest_framework.test import APITestCase


class ReplacerTests(APITestCase):
    def test_rep_correct(self):
        url = 'https://127.0.0.1:8000/api/my_word'
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "text": "my_word",
            "result": "[]"
        })