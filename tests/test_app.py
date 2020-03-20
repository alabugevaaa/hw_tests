# coding: utf-8
import unittest
import app
from unittest.mock import patch


class TestApp(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        self.error_doc = {"type": "insurance", "number": "10006"}
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_check_document_existance(self):
        exist = app.check_document_existance('2207 876234')
        self.assertTrue(exist)
        exist = app.check_document_existance('2207876234')
        self.assertFalse(exist)

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            owner = app.get_doc_owner_name()
            self.assertEqual(owner, 'Аристарх Павлов')
        with patch('app.input', return_value='0'):
            owner = app.get_doc_owner_name()
            self.assertIsNone(owner)

    def test_get_all_doc_owners_names(self):
        result = app.get_all_doc_owners_names()
        self.assertSetEqual(result, {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'})

    def test_move_doc_to_shelf(self):
        with patch('app.input', side_effect=['10006', '2']):
            app.move_doc_to_shelf()
        with patch('app.input', return_value='10006'):
            dir = app.get_doc_shelf()
            self.assertEqual(dir, '2')