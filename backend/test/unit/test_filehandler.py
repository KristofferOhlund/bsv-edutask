import json
import pytest 
import os

"""
Yield är som return men du kan fortsätta trots ditt return.
"""

class FileHandler:
    """This test demonstrates the use of yield as an alternative to return, which allows to write code *after* the statement
    which will be executed once all tests have run. This can be used for cleanup."""
    def __init__(self, filename):
        with open(filename, 'r') as readfile:
            self.file = json.load(readfile)

    def getContent(self):
        return self.file


class TestFileHandler:
    @pytest.fixture
    def test_fileHandler(self):
        data = {"Puppy": "Pepsi"}
        with open("file.json", "w") as file:
            json.dump(data, file)

        yield FileHandler("file.json")
        os.remove("file.json")

        
    @pytest.mark.json
    def test_getContent(self, test_fileHandler):
        data = test_fileHandler.getContent()
        assert data == {"Puppy": "Pepsi"}
