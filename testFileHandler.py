import unittest
import fileMessageHandler
import fileReceiverHandler
import os.path


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
        expected = True
        fileMessageHandler.createSourceCharacterFile(1)
        result = os.path.isfile("sourceCharacterFile.txt")
        self.assertEqual(result, expected)

    def test_createLocationListToFile(self):
        expected = True
        fileMessageHandler.createLocationListToFile(10_000)
        result = os.path.isfile('locationKeyFile.txt')
        self.assertEqual(result, expected)

    def test_createMessageListToFile(self):
        expected = True
        fileMessageHandler.createMessageListToFile(1_000_000)
        result = os.path.isfile('messageKeyFile.txt')
        self.assertEqual(result, expected)

    def test_loadMessageListFromFileLength(self):
        expected = 1_000_000
        list = []
        list = fileMessageHandler.loadMessageListFromFile()
        result = len(list)
        self.assertEqual(result, expected)

    def test_loadLocationListFromFileLength(self):
        expected = 10_000
        list = []
        list = fileMessageHandler.loadLocationListFromFile()
        result = len(list)
        self.assertEqual(result, expected)

    def test_searchIndexFromCharFile(self):
        expected = fileMessageHandler.searchIndexFromCharFile()

        list = fileMessageHandler.searchIndexFromCharFile()
        self.assertListEqual(list, expected)
        
    def test_findIndexByLocationFromMessage():
        fileReceiverHandler.findIndexByLocationFromMessage()

if __name__ == "__main__":

    unittest.main()
