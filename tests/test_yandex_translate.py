# coding: utf-8
import os
import unittest
import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = os.getenv('API_KEY')
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

class TestYaTrans(unittest.TestCase):
    def setUp(self):
        self.params = {
            'key': API_KEY,
            'text': 'привет',
            'lang': '{}-{}'.format('ru', 'en'),
        }

    def test_ok_status(self):
        response = requests.get(URL, params=self.params)
        self.assertEqual(response.status_code, 200)

    def test_not_ok_status(self):
        params = {
            'key': '',
            'text': 'привет',
            'lang': '{}-{}'.format('ru', 'en'),
        }
        response = requests.get(URL, params=params)
        self.assertNotEqual(response.status_code, 200)

    def test_translate(self):
        response = requests.get(URL, params=self.params)
        json_ = response.json()
        self.assertEqual(json_['text'][0], 'hi')
