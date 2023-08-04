import string
import random
import pickle
import logging
import os


def setLogger():
    numberOfHandledChar = 7
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='w')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)


def removeIndexFile():
    os.remove("indexFile.txt")


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
    # add mark for newline while reading sorce text if line is ending
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
    oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
    
    # change  own path in your computer to next line
    with open("sourceCharacterFile.txt", 'w') as charFile:
        while numberOfCharinFile < size:
            oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
            lengthOfOneLine = len(oneline)
            numberOfCharinFile += lengthOfOneLine
            print(lengthOfOneLine)
            print(numberOfCharinFile)
            charFile.write(oneline)
            oneline = ""

    with open(r"sourceCharacterFile.txt", 'r') as fp:        
        x = len(fp.readlines())
        logging.debug("Total lines  in char file: %s", str(x))

    charFile.close()  


def writeFinalMessageFileByNumber():
    """
    Create final message file by number. Set index by location to message 
    """

    listOfLocation=[] # load location from file to this list
    listOfMessage=[] # load messages and write after updating list
    listOfOneRowIndex=[] # read one row of index from file to this list
    
    lengthOfOneIndexRow = 0
    numberOfIndexRowInFile = 0
    currenLocationNumber = 0
    currenIndexNumber = 0
    locationCounter = 0 # count location together and set to final message by location 
    indexOfLocationList = 0

    logging.debug("writeFinalMessageFileByNumber func start ")
    listOfMessage = loadMessageListFromFile()
    logging.debug("oneMessagerow length : %s", str(len(listOfMessage)))
    with open("indexFile.txt", 'r') as indexFile:
            listOfLocation = loadLocationListFromFile()
            logging.debug("listOfOneRowLocation length : %s", str(len(listOfLocation)))
            indexRowLines = indexFile.readlines()
            print("index file readed")
            numberOfIndexRowInFile = len(indexRowLines)
            print("numberOfIndexRowInFile " + str(numberOfIndexRowInFile) +"\n")
            logging.debug("numberOfIndexRowInFile : %s", str(numberOfIndexRowInFile))
    
            for line in range(0,numberOfIndexRowInFile): # go through entire index file row by row
                logging.debug("line : %s", str(line))
                logging.debug("index file loop : %s", str(line))
                listOfOneRowIndex = [int(x) for x in indexRowLines[line].split(",")] # read one index row to list
                logging.debug("listOfOneRowIndex : %s", str(listOfOneRowIndex))
                lengthOfOneIndexRow = len(listOfOneRowIndex)

                for oneRowIndex in listOfOneRowIndex: # go through one index row and set numbers to message row by location
                    if lengthOfOneIndexRow > 100:
                        lastRowOfIndex = True

                    logging.debug("listOfOneRowIndex : %s", str(listOfOneRowIndex))
                    logging.debug("indexOfLocationList : %s", str(indexOfLocationList))
        
                    if indexOfLocationList > len(listOfLocation)-1:
                        logging.debug("length listOfOneRowLocation by index : %s", str(len(listOfLocation)-1))
                        logging.debug("length listOfOneRowLocation out of range :")
                        break

                    currenLocationNumber = listOfLocation[indexOfLocationList] # read one location from list
                    locationCounter += currenLocationNumber # count together location for message row
                    listOfMessage[locationCounter] = oneRowIndex # set index by location to message row
                    currenIndexNumber = oneRowIndex
                    
                    logging.debug("currenLocationNumber : %s", str(currenLocationNumber))
                    logging.debug("currenIndexNumber : %s", str(currenIndexNumber))
                    logging.debug("locationCounter : %s", str(locationCounter))
                    logging.debug("oneRowIndex : %s", str(oneRowIndex))
                    logging.debug("indexOfLocationList : %s", str(indexOfLocationList))

                    indexOfLocationList += 1 # add counter for reading next location From list
            indexFile.close()
            saveMessageToFile(listOfMessage)
    

def searchIndexFromCharFile():
    """
    Find index of letters(original message written by user)
    from sourceCharFile and create indexFile
    """
    listOfOneRowIndex=[] # list of index
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
    indexrowflineHandled = False
    
    logging.debug("searchIndexFromCharFile func start ")
    with open("indexFile.txt", 'w') as indexFile:
        with open("testMessage.txt", 'r') as messageFile:
            with open("sourceCharacterFile.txt", 'r') as charFile:
                numberOfRowsInCharfile = len(charFile.readlines())
                charFile.seek(0)
                logging.debug("Total lines  in charFile file : %s", str(numberOfRowsInCharfile))
                for readline in messageFile: # go through hole original message(write by user) file line by line
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
                            indexOfRowInCharFile +=1
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
                            listOfOneRowIndex.append(indexInCharSourceLine)
                            startSearchingIndex = oneCharcterGroupLength
                        elif numberOfHandledChar == 1: # set startseachindex for second char in row of sourcecharFile
                            startSearchingIndex =  2*oneCharcterGroupLength
                            listOfOneRowIndex.append(indexInCharSourceLine)
                        elif numberOfHandledChar == 2: # set startseachindex for third char in row of sourcecharFile
                            startSearchingIndex =  2*oneCharcterGroupLength
                            listOfOneRowIndex.append(indexInCharSourceLine)
                        numberOfHandledChar +=1
                       
                            
                        if(len(listOfOneRowIndex) == 100): # write row to file
                            indexFile.write(','.join(str(i) for i in listOfOneRowIndex)) # write row to file
                            indexFile.write("\n")
                            listOfOneRowIndex.clear()


                # end of file, set end mark(ô) for message
                indexInCharSourceLine = sourceCharacterlineHandler.find("ô", 0) # ô char means end of message, start searching from index zero of this mark 
                logging.debug("index found for ending message : %s", str(indexInCharSourceLine))
                indexrowrofile += str(indexInCharSourceLine)
                listOfOneRowIndex.append(indexInCharSourceLine)
                print(indexrowrofile)
                if indexrowflineHandled == False: # write last row of index
                    indexFile.write(','.join(str(i) for i in listOfOneRowIndex))
                    listOfOneRowIndex.clear()

            charFile.close()
        messageFile.close()
    indexFile.close()


def createLocationListToFile(lengthOfKey):
    locationList = []
    createdNumers = 0
    logging.debug("createLocationListToPickle func start")

    with open("locationKeyFile.txt", 'wb') as locationKeyFile:
        while createdNumers < lengthOfKey:
            locationList.append(random.randrange(1,100))
            createdNumers +=1
        pickle.dump(locationList, locationKeyFile)
    logging.debug("locationList length : %s", str(len(locationList)))    
    locationKeyFile.close()   

def loadLocationListFromFile():
    locationList = []

    with open ('locationKeyFile.txt', 'rb') as locationKeyFile:
        locationList = pickle.load(locationKeyFile)
    locationKeyFile.close()
    #print(locationList)
    return locationList

def createMessageListToFile(length):
    messageList = []
    createdNumers = 0
    logging.debug("createMessageListToFile func start")

    with open("messageKeyFile.txt", 'wb') as messageKeyFile:
        while createdNumers < length:
            messageList.append(random.randrange(1,309))
            createdNumers +=1
        pickle.dump(messageList, messageKeyFile)
    logging.debug("locationList length : %s", str(len(messageList)))    
    messageKeyFile.close()

def loadMessageListFromFile():
    messageList = []

    with open ('messageKeyFile.txt', 'rb') as messageKeyFile:
        messageList = pickle.load(messageKeyFile)
    messageKeyFile.close()
    return messageList


def saveMessageToFile(messageList):
    with open("messageKeyFile.txt", 'wb') as messageKeyFile:
        pickle.dump(messageList, messageKeyFile)
    logging.debug("locationList length : %s", str(len(messageList)))    
    messageKeyFile.close()
    messageList.clear()
    
def main():
    createLocationListToFile(10_000)
    createMessageListToFile(1_000_000)
    searchIndexFromCharFile()
    writeFinalMessageFileByNumber()

#setLogger()
#createLocationListToFile(10_000)
#createMessageListToFile(1_000_000)
#createOneSourceCharacterList()
#createSourceCharacterFile(1)
#searchIndexFromCharFile()
#writeFinalMessageFileByNumber()
#removeIndexFile()

if __name__ == "__main__":

    main()

