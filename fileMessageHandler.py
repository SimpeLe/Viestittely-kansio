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

def checkMessageCharacter(message):

    characters = string.ascii_letters + string.digits + string.punctuation +"äöåÄÖÅ" +'.' + "\n" + " " + "\t" + "\v" + "\r"
    print(characters)
    for i in message:
        if i in characters:
            print("char found")
            index = characters.find(i) # fi
            print(index)
            f = 6
        else:
            print("illegal char ")

def getMessageFromUI(message):
    logging.debug("getMessageFromUI func start")
   # checkMessageCharacter(message)
    logging.debug("message from UI : %s", str(message ))
    logging.debug("message length from UI : %s", str(len(message) ))
       
    file = Path(filePathOfFile+"/MyMessage.txt")
    result = file.is_file()
    if result:
        print("read ready message from user")
        realPath = filePathOfFile+"/MyMessage.txt"
        shutil.copy(realPath, "Message.txt")
    else:
        with open("Message.txt", 'w') as messageFile:
            messageFile.write(message)
            messageFile.close()


def getPathFromUI(path):
    global filePathOfFile
    #filePathOfFile = path
    filePathOfFile = "C:/Users/Ville/project/Viestittely-kansio/source" 
    logging.debug("filePathOfFile : %s", filePathOfFile)

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
            return # file does not exist
    
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
    listOfIndex=[] # index of original message
    currenLocationNumber = 0
    indexOfLocationList = 0

    logging.debug("writeFinalMessageFileByNumber func start ")
    listOfMessage = loadMessageListFromFile()
    #logging.debug("oneMessagerow length : %s", str(len(listOfMessage)))
    listOfIndex= searchIndexFromCharFile()
    listOfLocation = loadLocationListFromFile()
    #logging.debug("listOfLocation length : %s", str(len(listOfLocation)))
    
    for oneIndex in listOfIndex: # go through index list and set index  to message  by location
        
        #logging.debug("listOfIndex : %s", str(listOfIndex))
        #logging.debug("indexOfLocationList : %s", str(indexOfLocationList))

        currenLocationNumber = listOfLocation[indexOfLocationList] # read one location from locationList
        listOfMessage[currenLocationNumber] = oneIndex # set index by location to crypted message
        
        #logging.debug("currenLocationNumber : %s", str(currenLocationNumber))
        #logging.debug("oneIndex : %s", str(oneIndex))
        #logging.debug("indexOfLocationList : %s", str(indexOfLocationList))

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
    realPath = ""
    
    logging.debug("searchIndexFromCharFile func start ")
    with open("Message.txt", 'r') as messageFile: # open orinal message written by user
        realPath = filePathOfFile+ "/sourceCharacterFile.txt"
        with open(realPath, 'r') as charFile:
            numberOfRowsInCharfile = len(charFile.readlines())
            charFile.seek(0)
            #logging.debug("Total lines  in charFile file : %s", str(numberOfRowsInCharfile))
            for readline in messageFile: # go through hole original message(writing by user) file line by line
                #logging.debug("Total lines  in charFile file : %s", str(numberOfRowsInCharfile))
                messagelineHandler =  readline # set one row of message to handler
                logging.debug("messagelineHandler : %s", str(messagelineHandler))
                    
                for charInMsgLine in messagelineHandler: # go through entire row of original message char by char and found index from
                                                            # sourceCharFile
                    #logging.debug("number of  handled char in loop : %s", str(numberOfHandledChar))
                    
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
                       # logging.debug("indexOfRowInCharFile is : %s", str(indexOfRowInCharFile))
                        sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile] # load next sourceCharFile row after founding 3 index
                                                                                                # from one row (index == position of one character)        
                        #logging.debug("index of row in char file : %s", str(indexOfRowInCharFile))
                        lineHandled = True
                        
                    #logging.debug("handled char in loop : %s", str(numberOfHandledChar))
                    if charInMsgLine == "\n":
                        #logging.debug("char to be found is newline : %s", str(charInMsgLine))
                        d = 4
                    elif charInMsgLine == " ":
                        #logging.debug("char to be found is space : %s", str(charInMsgLine))
                        g = 7
                    else:
                      #  logging.debug("char to be found : %s", str(charInMsgLine))
                         h = 6
                  #  logging.debug("startSearchingIndex  : %s", str(startSearchingIndex ))
                    
                    if charInMsgLine == " " or charInMsgLine == "\t":
                        charInMsgLine = "è"
                    elif charInMsgLine == "\n" or charInMsgLine == "\v" or charInMsgLine == "\r":
                        charInMsgLine = "á"
                
                    indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine, startSearchingIndex) # find char index from sourceChar line
                    
               
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

            # end of original message file written by user , set end mark(ô) for message
            indexInCharSourceLine = sourceCharacterlineHandler.find("ô", 0) # ô char means end of message, start searching from index zero of this mark 
            logging.debug("index found for ending message : %s", str(indexInCharSourceLine))
            indexList.append(indexInCharSourceLine)
            #logging.debug("indexInCharSourceLine when finish sending  : %s", str(indexInCharSourceLine ))
            #logging.debug("indexList when finish sending  : %s", str(indexList ))
            #logging.debug("indexList length when finish sending  : %s", str(len(indexList) ))
            

        charFile.close()
    messageFile.close()
    removeMessageFile()
    indexList = addIndexWrap(indexList)
    return indexList

def addIndexWrap(indexList):
    logging.debug("addIndexWrap func start ")
    entireList = []
    indexWraplist = []
    wrappedIndex = 0
    counter = 0
    indexListLength = 0
    entireList = loadLocationListFromFile()
    indexWraplist = entireList[10_000:] # get index wrap list from entire list of locationKeyList and indexWrapList
    indexListLength = len(indexList)

    logging.debug("indexListLength: %s", str(indexListLength))
    logging.debug("indexWraplist[0]: %s", str(indexWraplist[0]))
    logging.debug("indexWraplist[1]: %s", str(indexWraplist[1]))
    logging.debug("indexWraplist[9998]: %s", str(indexWraplist[9998]))
    logging.debug("indexWraplist[9999]: %s", str(indexWraplist[9999]))

    for oneIndex in range(indexListLength): # go through index list and set index  wrapper
       
        # logging.debug("oneIndex: %s", str(oneIndex))
        # logging.debug("original index %s", str(indexList[oneIndex]))
        # logging.debug("Wrap index: %s", str(indexWraplist[oneIndex]))
        # logging.debug("Index together: %s", str(wrappedIndex))
        indexList[oneIndex] += indexWraplist[oneIndex]
       
        logging.debug("index after wrap: %s", str(indexList[oneIndex]))


    return indexList



def createLocationListToFile(lengthOfKey):
    """
    Create location lis for setting index to message
    and add index wrap list to the same list
    """
    locationList = []
    indexWrapList = []
    createdNumers = 0
    indexListLength = 10_000
    logging.debug("createLocationListtoFile func start")

    file = Path(filePathOfFile+"/locationKeyFile.txt")
    result = file.is_file()

    if result:
        difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

        if difference.days > 30: # create new every month
            logging.debug("Create new locationKeyFile")
        else:
            logging.debug("no locationKeyFile")
            #return

    indexWrapList = np.random.choice( range(0, 200), indexListLength, replace=True).tolist() 

    with open(filePathOfFile+"/locationKeyFile.txt", 'wb') as locationKeyFile:
        locationList = np.random.choice( range(0, 999999), lengthOfKey, replace=False).tolist() # creatue unique list on numbers (amount is lengthOfKey)
                                                                                                # in range 0-999 999 (length of crypted message)        
        print("locationList length 1: %s", str(len(locationList)))
        locationList += indexWrapList
        print("locationList length 2: %s", str(len(locationList)))
        pickle.dump(locationList, locationKeyFile)
      
    locationKeyFile.close()   

def loadLocationListFromFile():
    """
    Load location list when creating new message
    """
    logging.debug("loadLocationListFromFile func start")
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
    """
    Create message list for writing message. This list will be updated every time
    while creting a new message
    """
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
    """
    Load this list to use when creting final message
    """
    messageList = []

    with open ('messageFile.txt', 'rb') as messageKeyFile:
        messageList = pickle.load(messageKeyFile)
    messageKeyFile.close()
    return messageList


def saveMessageToFile(messageList):
    """
    Save ready message to file for sending
    """

    destination = filePathOfFile+"\\messageFile.txt"
    logging.debug("saveMessageToFile func start")
    with open("messageFile.txt", 'wb') as messageFile:
        pickle.dump(messageList, messageFile)
    logging.debug("messageList length : %s", str(len(messageList)))    
    messageFile.close()
    messageList.clear()
    
    currPath = str(Path.cwd())
    currPath =  currPath.replace('\\', '/')
    if currPath == filePathOfFile:
        print("same path")
        logging.debug("same path")
        logging.debug("destination path : %s", str(destination)) 
    else:
        print("different path")
        shutil.copyfile("messageFile.txt", destination)

def createMessage():
    createSourceCharacterFile(1)
    createLocationListToFile(10_000)
    createMessageListToFile(1_000_000)
    writeFinalMessageFileByNumber()
    
def main():
    
    #getPathFromUI(path)
    #printFilePathFromUI()
    setLogger()
    getPathFromUI("grth")
    #createLocationListToFile(10_000)
    getMessageFromUI("bhdghb")
    createMessage()
    #createOneSourceCharacterList()
    
if __name__ == "__main__":

    main()

