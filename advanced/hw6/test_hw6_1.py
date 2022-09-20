
import unittest
from unittest.mock import patch
from hw6_1 import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, delete_doc

class TestSomething(unittest.TestCase):

    def test_check_document_existance_1(self):
        self.assertTrue(check_document_existance('2207 876234'))

    def test_check_document_existance_2(self):
        self.assertFalse(check_document_existance('2207'))

    @patch('builtins.input', return_value="2207 876234")
    def test_get_doc_owner_name_1(self, mock_input):
        self.assertEqual(get_doc_owner_name(), "Василий Гупкин")

    @patch('builtins.input', return_value="2207 ")
    def test_get_doc_owner_name_2(self, mock_input):
        self.assertFalse(get_doc_owner_name())

    def test_get_all_doc_owners_names(self) :
        self.assertEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'})

    @patch('builtins.input', return_value="2207 876234")
    def test_delete_doc(self, mock_input) :
        self.assertEqual(delete_doc(), ('2207 876234', True))
        









if __name__ == '__main__':
    unittest.main()









