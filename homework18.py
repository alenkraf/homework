#Task1
import unittest
from homework13 import TVController

class TestTVController(unittest.TestCase):

    def setUp(self):
        self.controller = TVController(["BBC", "Discovery", "TV1000"])

    def test_first_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(self.controller.last_channel(), "TV1000")

    def test_turn_channel_valid(self):
        self.assertEqual(self.controller.turn_channel(2), "Discovery")

    def test_turn_channel_invalid(self):
        self.assertEqual(self.controller.turn_channel(4), "BBC")

    def test_next_channel(self):
        self.assertEqual(self.controller.next_channel(), "Discovery")

    def test_previous_channel(self):
        self.assertEqual(self.controller.previous_channel(), "BBC")

    def test_current_channel(self):
        self.assertEqual(self.controller.current_channel(), "BBC")

    def test_exists_by_number_valid(self):
        self.assertEqual(self.controller.exists(2), "Yes")

    def test_exists_by_number_invalid(self):
        self.assertEqual(self.controller.exists(4), "No")

    def test_exists_by_name_valid(self):
        self.assertEqual(self.controller.exists("BBC"), "Yes")

    def test_exists_by_name_invalid(self):
        self.assertEqual(self.controller.exists("HBO"), "No")

if __name__ == '__main__':
    unittest.main()



#Task2
import unittest
from os import path
import lesson10.module as pb
import json

class ExistanceChecker:

    def is_file_exist(self, filepath : str):
        return path.exists(filepath)
    
    def checker(self, filepath):
        result = self.is_file_exist(filepath)
        if result:
            return 1
        else:
            return 0

class TestPhoneBookMaking(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file = "test_phonebook.json"

    def test_make_phonebook(self):
        pb.make_phonebook(self.test_file)
        ch = ExistanceChecker()
        self.assertEqual(ch.checker(self.test_file), 1)

class TestPhoneBookTools(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file = "test_phonebook.json"

    def test_add_record(self):
        pb.add_record("Name", "Surename", "0937155515", "Zviahel", self.test_file)
        with open(self.test_file) as read_test:
            content = json.load(read_test)
            self.assertEqual(content[len(content) - 1], {"first_name": "Name", "last_name": "Surename", "tel_number": "0937155515", "city": "Zviahel"})
    
    def test_find_record(self):
        result = pb.find_record("Name", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Surename", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("0937155515", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Zviahel", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Name Surename", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("qaswedfr", self.test_file)
        self.assertEqual(result, 2)
    
    def test_update_record(self):
        pb.update_record("0937155515", "0932070323", self.test_file)
        with open(self.test_file) as read_test:
            content = json.load(read_test)
            self.assertEqual(content[0]["tel_number"], "0932070323")

    def test_delete_record(self):
        pb.delete_record("0932070323", self.test_file)
        result = pb.find_record("0932070323", self.test_file)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()