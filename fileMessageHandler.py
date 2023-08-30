import string
import random
import pickle
import os
import datetime
import numpy as np # pip install numpy
from pathlib import Path
import shutil


def checkMessageCharacter(message):
    """
    Check if message contains illegal character
    """

    legalCharacters = string.ascii_letters + string.digits + string.punctuation +"äöåÄÖÅ" +'.' + "\n" + " " + "\t" + "\v" + "\r"
    
    for char in message:
        if char not in legalCharacters:
            message = message.replace(char, '_')
    return message


def getMessageFromUI(message):
    """
    Receive original message from UI or read users pre-defined
    message from file MyMessage.txt
    """
       
    file = Path(filePathOfFile+"/MyMessage.txt")
    result = file.is_file()
    if result:
        realPath = filePathOfFile+"/MyMessage.txt"
        with open( realPath,"r+") as f:
            message = f.read()
            message = checkMessageCharacter(message)
            
            with open( "Message.txt","w") as file:
                if len(message) > 10_000: 
                    allowedMessage = message[:10_000] # max. message lentgh is 10 000
                    file.write(allowedMessage)
                else:
                    file.write(message)
                
                f.close()
                file.close()
    else:
        with open("Message.txt", 'w') as messageFile:
            messageFile.write(message)
            messageFile.close()
   

def getPathFromUI(path):
    """
    Get user selected foldef from UI which contain key files
    
    """
    global filePathOfFile
    filePathOfFile = path


def removeMessageFile():
    """
    Revomeve message after it has been handled
    """
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

        if difference.days < 30: 
            return # file does exist and is under than 30 days old

    
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

    listOfMessage = loadMessageListFromFile()
    listOfIndex= searchIndexFromCharFile()
    listOfLocation = loadLocationListFromFile()
    
    
    for oneIndex in listOfIndex: # go through index list and set index  to message  by location
        
        currenLocationNumber = listOfLocation[indexOfLocationList] # read one location from locationList
        listOfMessage[currenLocationNumber] = oneIndex # set index by location to crypted message

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
    

    with open("Message.txt", 'r') as messageFile: # open orinal message written by user
        realPath = filePathOfFile+ "/sourceCharacterFile.txt"
        with open(realPath, 'r') as charFile:
            numberOfRowsInCharfile = len(charFile.readlines())
            charFile.seek(0)
            
            for readline in messageFile: # go through hole original message(writing by user) file line by line
                
                messagelineHandler =  readline # set one row of message to handler
                    
                for charInMsgLine in messagelineHandler: # go through entire row of original message char by char and found index from
                                                            # sourceCharFile
                    
                    
                    if numberOfHandledChar == numberOfCharHandle: # when found 3 index from one row of sourceCharFile load next row
                                                                    # of sourcecharFile by adding 1 to indexOfRowInCharFile
                        lineHandled = False
                        numberOfHandledChar = 0
                        indexOfRowInCharFile +=1 # increase for reading next row
                        startSearchingIndex = 0
                    if lineHandled == False:  # this refers to reading and handling one source Character row
                        charFile.seek(0) #  set file iterator to zero before read line, otherwise it will raise "index out of range" error
                        if numberOfRowsInCharfile == indexOfRowInCharFile: # end of file, start reading from first row
                            indexOfRowInCharFile = 0
                       
                        sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile] # load next sourceCharFile row after founding 3 index
                                                                                                # from one row (index == position of one character)        
                        lineHandled = True
                        
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
            indexList.append(indexInCharSourceLine)
            

        charFile.close()
    messageFile.close()
    removeMessageFile()
    indexList = addIndexWrap(indexList)
    return indexList

def addIndexWrap(indexList):
    """
    Add random number between 1-100 to each index berore sendin message
    """
    
    entireList = [] # entire locatioKey list
    indexWraplist = [] #¤ list of wrap value
    indexListLength = 0
    entireList = loadLocationListFromFile()
    indexWraplist = entireList[10_000:] # get index wrap list from entire list of locationKeyList and indexWrapList
    indexListLength = len(indexList)


    for oneIndex in range(indexListLength): # go through index list and set index  wrapper
       
        indexList[oneIndex] += indexWraplist[oneIndex]
       
    return indexList



def createLocationListToFile(lengthOfKey):
    """
    Create location list for setting index to message
    and add index wrap list to the same list
    """
    locationList = []
    indexWrapList = []
    createdNumers = 0
    indexListLength = 10_000

    file = Path(filePathOfFile+"/locationKeyFile.txt")
    result = file.is_file()

    if result:
        difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

        if difference.days < 30: # create new every month
            return # under 30 days old, do not create new one, return

    indexWrapList = np.random.choice( range(0, 100), indexListLength, replace=True).tolist() 

    with open(filePathOfFile+"/locationKeyFile.txt", 'wb') as locationKeyFile:
        locationList = np.random.choice( range(0, 999999), lengthOfKey, replace=False).tolist() # creatue unique list on numbers (amount is lengthOfKey)
                                                                                                # in range 0-999 999 (length of crypted message)        
    
        locationList += indexWrapList
        pickle.dump(locationList, locationKeyFile)
      
    locationKeyFile.close()   

def loadLocationListFromFile():
    """
    Load location list when creating new message
    """
    locationList = []
    
    file = Path(filePathOfFile+"/locationKeyFile.txt")
    result = file.is_file()

    if result:

        with open (filePathOfFile+"/locationKeyFile.txt", 'rb') as locationKeyFile:
            locationList = pickle.load(locationKeyFile)
        locationKeyFile.close()
    else:
        return #location key file does not exist

    return locationList

def createMessageListToFile(length):
    """
    Create message list for writing message. This list will be updated every time
    while creting a new message
    """
    messageList = []
    createdNumers = 0

    with open("messageFile.txt", 'wb') as messageKeyFile:
        while createdNumers < length:
            messageList.append(random.randrange(1,308))
            createdNumers +=1
        pickle.dump(messageList, messageKeyFile)  
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

    with open("messageFile.txt", 'wb') as messageFile:
        pickle.dump(messageList, messageFile)

    messageFile.close()
    messageList.clear()
    
    currPath = str(Path.cwd())
    currPath =  currPath.replace('\\', '/')
    if currPath == filePathOfFile:
        #same path
        h = 7
    else:
        shutil.copyfile("messageFile.txt", destination)
        os.remove("messageFile.txt") 

def createMessage():
    createSourceCharacterFile(1)
    createLocationListToFile(10_000)
    createMessageListToFile(1_000_000)
    writeFinalMessageFileByNumber()
    
def main():
    pass
    
if __name__ == "__main__":

    main()

