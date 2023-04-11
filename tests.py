from django.test import TestCase
from rest_framework.test import APIClient

from polls.factories import QuestionFactiory


class MyTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # super(self).setUp()
    def test_1(self):
        resp = self.client.get('/404')
        self.assertEqual(resp.status_code, 404)
    def test_2(self):
        QuestionFactiory()
        resp = self.client.get('/api/v1/question-list/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), [])
        self.ass
