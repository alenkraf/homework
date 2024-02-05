import logging
import unittest
import os
import pytest

class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        logging.info(f"File {self.filename} opened. Counter: {self.counter}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        self.counter -= 1
        logging.info(f"File {self.filename} closed. Counter: {self.counter}")

        if exc_type is not None:
            logging.error(f"An error occurred: {exc_type}, {exc_value}, {traceback}")
            return False
        return True
with CustomFileManager("example.txt", "r") as file:
    content = file.read()
    print(content)

class TestCustomFileManager(unittest.TestCase):
    def test_file_reading(self):
        with CustomFileManager("test_file.txt", "w") as file:
            file.write("Hello, World!")

        with CustomFileManager("test_file.txt", "r") as file:
            content = file.read()
            self.assertEqual(content, "Hello, World!")

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            with CustomFileManager("nonexistent_file.txt", "r") as file:
                content = file.read()

if __name__ == '__main__':
    unittest.main()

@pytest.fixture
def custom_file_manager_fixture():
    with CustomFileManager("fixture_file.txt", "w") as file:
        file.write("Fixture data")
    yield file

def test_custom_logic_with_file(custom_file_manager_fixture):
    content = custom_file_manager_fixture.read()
    assert content == "Fixture data"



