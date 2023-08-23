import unittest
import fileMessageHandler
import fileReceiverHandler
import os.path
from pathlib import Path


class TestHandler(unittest.TestCase):

    def test_createOneSourceCharacterListLength(self):
        expected = 103
        res = fileMessageHandler.createOneSourceCharacterList()
        result = len(res)
        self.assertEqual(result, expected)

    def test_createOneSourceCharacterListLegalCharacter(self):
        expected = True
        res = fileMessageHandler.createOneSourceCharacterList()
        result = "a" in res
        self.assertEqual(result, expected)

    def test_createOneSourceCharacterListIllegalCharacter(self):
        expected = True
        res = fileMessageHandler.createOneSourceCharacterList()
        result = "û" in res
        self.assertFalse(result, expected)

    def test_createSourceCharacterFile(self):
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = True
        fileMessageHandler.createSourceCharacterFile(1)
        result = os.path.isfile("sourceCharacterFile.txt")
        self.assertEqual(result, expected)

    def test_createLocationListToFile(self):
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = True
        fileMessageHandler.createLocationListToFile(10_000)
        result = os.path.isfile('locationKeyFile.txt')
        self.assertEqual(result, expected)

    def test_createMessageListToFile(self):
        #fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = True
        fileMessageHandler.createMessageListToFile(1_000_000)
        result = os.path.isfile('messageFile.txt')
        self.assertEqual(result, expected)

    def test_loadMessageListFromFileLength(self):
        # precondition: set removeMessageFile() to comment in function 
        # searchIndexFromCharFile in file fileReceiverHandler
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = 1_000_000
        list = []
        list = fileMessageHandler.loadMessageListFromFile()
        result = len(list)
        self.assertEqual(result, expected)

    def test_loadLocationListFromFileLength(self):
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = 20_000
        list = []
        list = fileMessageHandler.loadLocationListFromFile()
        result = len(list)
        self.assertEqual(result, expected)

    def test_searchIndexFromCharFile(self):
        # precondition: set removeMessageFile() to comment in function searchIndexFromCharFile
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        expected = fileMessageHandler.searchIndexFromCharFile()

        list = fileMessageHandler.searchIndexFromCharFile()
        self.assertListEqual(list, expected)
        
    def test_findIndexByLocationFromMessage(self):
        #fileMessageHandler.getPathFromUI(str(Path.cwd()))
        fileMessageHandler.createMessageListToFile(1_000_000)

        fileReceiverHandler.getPathFromUI(str(Path.cwd()))
        expected = 10_000
        list = []
        list = fileReceiverHandler.findIndexByLocationFromMessage()
        result = len(list)
        self.assertEqual(result, expected)

    def test_addIndexWrap(self):
        fileMessageHandler.getPathFromUI(str(Path.cwd()))
        wrappedList = []
        list = fileMessageHandler.searchIndexFromCharFile()
        wrappedList = fileMessageHandler.addIndexWrap(list)
        self.assertEqual(wrappedList, list)


if __name__ == "__main__":

    unittest.main()
