import unittest
import fileMessageHandler
import fileReceiverHandler
import os.path


class TestHandler(unittest.TestCase):


    def test_createOneSourceCharacterList(self):
        expected = 103
        res = fileMessageHandler.createOneSourceCharacterList()
        result = len(res)
        self.assertEqual(result, expected)

    def test_createOneSourceCharacterListCharacter(self):
        expected = True
        res = fileMessageHandler.createOneSourceCharacterList()
        result = "a" in res
        self.assertEqual(result, expected)

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

    def test_loadMessageListFromFile(self):
        expected = 1_000_000
        list = []
        list = fileMessageHandler.loadMessageListFromFile()
        result = len(list)
        self.assertEqual(result, expected)

    

if __name__ == "__main__":

    unittest.main()
