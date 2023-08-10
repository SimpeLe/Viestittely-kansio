import string
import random
import pickle
import logging
import os
import datetime
import numpy as np # pip install numpy
from pathlib import Path
import shutil


def setLogger():
    
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='w')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)

def createUniqueList():
    list_of_numbers = np.random.choice(
    range(1, 999999),
    1112,
    replace=False
    ).tolist()

    print(list_of_numbers) 


def getMessageFromUI(message):
       
    file = Path(filePathOfFile+"/MyMessage.txt")
    result = file.is_file()
    if result:
        print("read ready message from user")
        realPath = filePathOfFile+"/MyMessage.txt"
        with open("Message.txt", 'w') as messageFile:
            messageFile.write(message)
            shutil.copy(realPath, "Message.txt")
            messageFile.close()
    
    else:
        with open("Message.txt", 'w') as messageFile:
            messageFile.write(message)
            messageFile.close()


def getPathFromUI(path):
    global filePathOfFile
    filePathOfFile = path
    logging.debug("filePathOfFile : %s", filePathOfFile)
    print(filePathOfFile)

def getCreationtime():
    file = "sourceCharacterFile.txt"
 
    print("Created")
    print(os.path.getctime(file))
    print(datetime.datetime.fromtimestamp(os.path.getctime(file)))

    today = datetime.datetime.now()
    print(today)

    difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

    print(difference)
    if difference.days > 30:
        print("over 30")
        return
 
    print("Modified")
    print(os.path.getmtime(file))
    print(datetime.datetime.fromtimestamp(os.path.getmtime(file)))

def removeMessageFile():
    os.remove("Message.txt")


def createOneSourceCharacterList():
    """
    Creates list of all alphabetic ascii
    characters in arbitrary order 
    """
   
    # Create list of all characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # add scandinavian characters
    characters +="äöåÄÖÅ"
    # add space characters while reading message text if space
    characters += "è"
    # add mark for newline while reading message text if line is ending
    characters += "á"
    # add mark for ending original message
    characters += "ô"
    
    # Randomize order of string
    randomString = ''.join(random.sample(characters, len(characters)))
    
    return randomString

def createSourceCharacterFile(size):
    """
    Creates parameter "size" Mbyte sizes file which inludes
    all alphabetic ascii characters in 
    arbitrary order 
    """
    # size in megabytes
    size = size* 1_024_000
    # length of one line which added to file 
    lengthOfOneLine = 0
    # numuber of rows in file
    numberOfRows = 0
    # number of character in file
    numberOfCharinFile = 0

   
    file = Path(filePathOfFile+"/sourceCharacterFile.txt")
    result = file.is_file()
    
    if result:
        difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

        if difference.days > 30: # create new every month
            logging.debug("Create new sourceCharFile")
        else:
            return
    
    # change  own path in your computer to next line
    
    with open(filePathOfFile+"/sourceCharacterFile.txt", 'w') as charFile:
        while numberOfCharinFile < size:
            oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
            lengthOfOneLine = len(oneline)
            numberOfCharinFile += lengthOfOneLine
            charFile.write(oneline)
            oneline = ""

    charFile.close()  


def writeFinalMessageFileByNumber():
    """
    Create final message file by number. Set index by location to message 
    """

    listOfLocation=[] # load location from file to this list
    listOfMessage=[] # load messages and write after updating list
    listOfIndex=[]
    lengthOfOneIndexRow = 0
    numberOfIndexRowInFile = 0
    currenLocationNumber = 0
    currenIndexNumber = 0
    locationCounter = 0 # count location together and set to final message by location 
    indexOfLocationList = 0

    logging.debug("writeFinalMessageFileByNumber func start ")
    listOfMessage = loadMessageListFromFile()
    logging.debug("oneMessagerow length : %s", str(len(listOfMessage)))
    #with open("indexFile.txt", 'r') as indexFile:
    listOfIndex= searchIndexFromCharFile()
    listOfLocation = loadLocationListFromFile()
    logging.debug("listOfOneRowLocation length : %s", str(len(listOfLocation)))
    #indexRowLines = indexFile.readlines()
    print("index file readed")
    #numberOfIndexRowInFile = len(indexRowLines)
    print("numberOfIndexRowInFile " + str(numberOfIndexRowInFile) +"\n")
    #logging.debug("numberOfIndexRowInFile : %s", str(numberOfIndexRowInFile))

    for oneIndex in listOfIndex: # go through one index row and set numbers to message row by location
        if lengthOfOneIndexRow > 100:
            lastRowOfIndex = True

        logging.debug("listOfIndex : %s", str(listOfIndex))
        logging.debug("indexOfLocationList : %s", str(indexOfLocationList))

        # if indexOfLocationList > len(listOfLocation)-1:
        #     logging.debug("length listOfOneRowLocation by index : %s", str(len(listOfLocation)-1))
        #     logging.debug("length listOfOneRowLocation out of range :")
        #     break

        currenLocationNumber = listOfLocation[indexOfLocationList] # read one location from list
        locationCounter += currenLocationNumber # count together location for message row
        listOfMessage[locationCounter] = oneIndex # set index by location to message row
        currenIndexNumber = oneIndex
        
        logging.debug("currenLocationNumber : %s", str(currenLocationNumber))
        logging.debug("currenIndexNumber : %s", str(currenIndexNumber))
        logging.debug("locationCounter : %s", str(locationCounter))
        logging.debug("oneRowIndex : %s", str(oneIndex))
        logging.debug("indexOfLocationList : %s", str(indexOfLocationList))

        indexOfLocationList += 1 # add counter for reading next location From list
    listOfIndex.clear()
    saveMessageToFile(listOfMessage)
    

def searchIndexFromCharFile():
    """
    Find index of letters(original message written by user)
    from sourceCharFile and create indexFile
    """
    
    indexList=[] # list of index
    sourceCharacterlineHandler  = "" # read one row of character to this 
    indexInCharSourceLine = 0 # number of index found from row
    startSearchingIndex = 0 # start index when finding index from row
    indexOfRowInCharFile = 0 # current row number while proceeding sourceCharFile
    numberOfRowsInCharfile = 0 # numberd of rows in char file, when reach end set indexOfRowInCharFile to zero
    oneCharcterGroupLength = 103
    numberOfCharHandle = 3 # search 3 cracter from each sorcecharacterRow
    numberOfHandledChar = 0
    messagelineHandler = "" # contains one line of original message
    lineHandled = False
    indexrowrofile = ""
    realPath = ""
    
    logging.debug("searchIndexFromCharFile func start ")
    with open("Message.txt", 'r') as messageFile:
        realPath = filePathOfFile+ "/sourceCharacterFile.txt"
        print("realPath")
        #with open("sourceCharacterFile.txt", 'r') as charFile:
        with open(realPath, 'r') as charFile:
            numberOfRowsInCharfile = len(charFile.readlines())
            charFile.seek(0)
            logging.debug("Total lines  in charFile file : %s", str(numberOfRowsInCharfile))
            for readline in messageFile: # go through hole original message(writing by user) file line by line
                logging.debug("Total lines  in charFile file : %s", str(numberOfRowsInCharfile))
                messagelineHandler =  readline # set one row of message to handler
                logging.debug("messagelineHandler : %s", str(messagelineHandler))
                    
                for charInMsgLine in messagelineHandler: # go through entire row of original message char by char and found index from
                                                            # sourceCharFile
                    logging.debug("handled char in loop : %s", str(numberOfHandledChar))
                    
                    if numberOfHandledChar == numberOfCharHandle: # when found 3 index from one row of sourceCharFile load next row
                                                                    # of sourcecharFile by adding 1 to indexOfRowInCharFile
                        lineHandled = False
                        numberOfHandledChar = 0
                        indexOfRowInCharFile +=1 # increase for reading next row
                        startSearchingIndex = 0
                    if lineHandled == False:  # this refers to reading and handling one source Character row
                        charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                        if numberOfRowsInCharfile == indexOfRowInCharFile: # end of file, start reading from first row
                            indexOfRowInCharFile = 0

                        sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile] # load next sourceCharFile row after founding 3 index
                                                                                                # from one row (index == position of one character)        
                        logging.debug("index of row in char file : %s", str(indexOfRowInCharFile))
                        lineHandled = True
                        
                    logging.debug("handled char in loop : %s", str(numberOfHandledChar))
                    logging.debug("char to be found : %s", str(charInMsgLine))
                    logging.debug("startSearchingIndex  : %s", str(startSearchingIndex ))
                    
                    if charInMsgLine == " " or charInMsgLine == "\t":
                        charInMsgLine = "è"
                    elif charInMsgLine == "\n" or charInMsgLine == "\v" or charInMsgLine == "\r":
                        charInMsgLine = "á"
                

                    indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine, startSearchingIndex) # find char index from sourceChar line
                    logging.debug("index found : %s", str(indexInCharSourceLine))

                    
                    if numberOfHandledChar == 0:
                        indexList.append(indexInCharSourceLine)
                        startSearchingIndex = oneCharcterGroupLength
                    elif numberOfHandledChar == 1: # set startseachindex for second char in row of sourcecharFile
                        startSearchingIndex =  2*oneCharcterGroupLength
                        indexList.append(indexInCharSourceLine)
                    elif numberOfHandledChar == 2: # set startseachindex for third char in row of sourcecharFile
                        startSearchingIndex =  2*oneCharcterGroupLength
                        indexList.append(indexInCharSourceLine)
                    
                    numberOfHandledChar +=1

            # end of file, set end mark(ô) for message
            indexInCharSourceLine = sourceCharacterlineHandler.find("ô", 0) # ô char means end of message, start searching from index zero of this mark 
            logging.debug("index found for ending message : %s", str(indexInCharSourceLine))
            indexrowrofile += str(indexInCharSourceLine)
            indexList.append(indexInCharSourceLine)
            

        charFile.close()
    messageFile.close()
    removeMessageFile()
    return indexList


def createLocationListToFile(lengthOfKey):
    locationList = []
    createdNumers = 0
    logging.debug("createLocationListtoFile func start")

    file = Path(filePathOfFile+"/locationKeyFile.txt")
    result = file.is_file()

    if result:
        difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

        if difference.days > 30: # create new every month
            logging.debug("Create new locationKeyFile")
        else:
            return

    with open(filePathOfFile+"/locationKeyFile.txt", 'wb') as locationKeyFile:
        while createdNumers < lengthOfKey:
            locationList.append(random.randrange(1,100))
            createdNumers +=1
        pickle.dump(locationList, locationKeyFile)
    logging.debug("locationList length : %s", str(len(locationList)))    
    locationKeyFile.close()   

def loadLocationListFromFile():
    locationList = []
    

    file = Path(filePathOfFile+"/locationKeyFile.txt")
    result = file.is_file()

    if result:

        with open (filePathOfFile+"/locationKeyFile.txt", 'rb') as locationKeyFile:
            locationList = pickle.load(locationKeyFile)
        locationKeyFile.close()
    else:
        print("location key file does not exist")
        return

    return locationList

def createMessageListToFile(length):
    messageList = []
    createdNumers = 0
    logging.debug("createMessageListToFile func start")

    with open("messageFile.txt", 'wb') as messageKeyFile:
        while createdNumers < length:
            messageList.append(random.randrange(1,309))
            createdNumers +=1
        pickle.dump(messageList, messageKeyFile)
    logging.debug("messageList length : %s", str(len(messageList)))    
    messageKeyFile.close()

def loadMessageListFromFile():
    messageList = []

    with open ('messageFile.txt', 'rb') as messageKeyFile:
        messageList = pickle.load(messageKeyFile)
    messageKeyFile.close()
    return messageList


def saveMessageToFile(messageList):
    with open("messageFile.txt", 'wb') as messageFile:
        pickle.dump(messageList, messageFile)
    logging.debug("messageList length : %s", str(len(messageList)))    
    messageFile.close()
    messageList.clear()
    
def main():
    
    #getMessageFromUI(message)
    #createUniqueList()
    #getPathFromUI()
    #getPathFromUI(path)
    #printFilePathFromUI()
    #getCreationtime()
    getPathFromUI("grth")
    createSourceCharacterFile(1)
    createLocationListToFile(10_000)
    createMessageListToFile(1_000_000)
    getMessageFromUI("bhdghb")
    writeFinalMessageFileByNumber()
    #searchIndexFromCharFile()
    #writeFinalMessageFileByNumber()
    #createOneSourceCharacterList()

#setLogger()
#createLocationListToFile(10_000)
#createMessageListToFile(1_000_000)
    #getPathFromUI("grth")
    #createSourceCharacterFile(1)
#searchIndexFromCharFile()
#writeFinalMessageFileByNumber()
#removeIndexFile()

if __name__ == "__main__":

    main()

