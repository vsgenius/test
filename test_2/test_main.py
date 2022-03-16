import unittest
from yandexdiskapi import YandexDiskApi


TOKEN = ' '
HEADERS = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
PATH='/Netology_CourseWork_1/'
ya = YandexDiskApi('Yandex_Test')


class TestYandexUnittest(unittest.TestCase):

    def test_satus_code(self):
        self.assertEqual(200, ya.check_token(TOKEN, HEADERS))
        pass

    def test_create_folder(self):
        self.assertEqual(True, ya.get_folder(PATH,HEADERS))

