import unittest
from accounting import people, shelf, list_shelf, \
    list_doc, add_doc, delete, add_shelf, move, find_dir_val, find_dir_key

DOCUMENTS = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
DIRECTORIES = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


class TestAccountingUnittest(unittest.TestCase):

    def test_people(self):
        self.assertEqual(True, people('2207 876234'))
        self.assertEqual(False, people('555'))

    def test_shelf(self):
        self.assertEqual(True, shelf('2207 876234'))
        self.assertEqual(False, shelf('222'))

    def test_add_doc(self):
        self.assertEqual(True, add_doc('111', 'passport', 'Владимир Иванов', '1'))
        self.assertEqual(False, add_doc('444', 'insurance', 'Владимир Иванов', '4'))

    def test_delete(self):
        self.assertEqual(True, delete('10006'))
        self.assertEqual(False, delete('333'))

    def test_move(self):
        self.assertEqual(True, move('2207 876234', '3'))
        self.assertEqual(False, move('2207 876234', '4'))

    def test_add_shelf(self):
        self.assertEqual(True, add_shelf('5'))
        self.assertEqual(False, add_shelf('1'))

    def test_find_dir_key(self):
        self.assertEqual(True, find_dir_key('1'))
        self.assertEqual(False, find_dir_key('6'))
