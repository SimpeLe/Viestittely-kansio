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

    legalCharacters = string.ascii_letters + string.digits + string.punctuation +"äöåÄÖÅ" +'.' + "“”’" + "\n" + " " + "\t" + "\v" + "\r"
    
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
        with open( realPath,"r+", errors='ignore') as f: # encoding='utf-8'
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
    # add american style apostrophe and quotation marks
    characters += "“”’"
    # add space characters while reading message text if space
    characters += "è"
    # add mark for newline while reading message text if line is ending
    characters += "á"
    # add mark for ending original message
    characters += "ô"

    # Randomize order of string
    randomString = ''.join(random.sample(characters, len(characters)))

    return randomString


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
    listOfIndex= searchIndexFromCharList()
    listOfLocation = loadLocationListFromFile()
    listOfLocation = listOfLocation[:10_000]
    
    for oneIndex in listOfIndex: # go through index list and set index  to message  by location
        
        currenLocationNumber = listOfLocation[indexOfLocationList] # read one location from locationList
        listOfMessage[currenLocationNumber] = oneIndex # set index by location to crypted message

        indexOfLocationList += 1 # add counter for reading next location From list
    listOfIndex.clear()
    saveMessageToFile(listOfMessage)
    

def searchIndexFromCharList():
    """
    Find index of letters(original message written by user)
    from sourceCharFile and create indexFile
    """

    indexList=[] # list of index
    indexInCharSourceList = 0 # number of index found from list
    indexForMessageList = 0 # the real number to set in final message
    startSearchingIndex = 0 # start index when finding index from row
    messagelineHandler = "" # contains one line of original message
    lengthOfOneCharacterSet = 0 # length og one source character set
    realPath = ""
    entireList=[]
    sourceCharList = []
    

    with open("Message.txt", 'r') as messageFile: # open orinal message written by user
        realPath = filePathOfFile+ "/keyFile.txt"
        with open(realPath, 'rb') as keyFile:
            entireList = pickle.load(keyFile)
            sourceCharList = entireList[20_000:]
            lengthOfOneCharacterSet = len(createOneSourceCharacterList())
            
            for readline in messageFile: # go through hole original message(writing by user) file line by line
                
                messagelineHandler =  readline # set one row of message to handler
                for charInMsgLine in messagelineHandler: # go through entire row of original message char by char and found index from
                                                            # sourceCharList
                                           
                    if charInMsgLine == " " or charInMsgLine == "\t":
                        charInMsgLine = "è"
                    elif charInMsgLine == "\n" or charInMsgLine == "\v" or charInMsgLine == "\r":
                        charInMsgLine = "á"
                    
                   
                    indexInCharSourceList = sourceCharList.index(charInMsgLine, startSearchingIndex) # find char index from sourceChar list
                    indexForMessageList = indexInCharSourceList - startSearchingIndex # count index for message list
                    indexList.append(indexForMessageList)
                    startSearchingIndex += lengthOfOneCharacterSet # increase this for searching from next char set each time
                    

            
            indexInCharSourceList = sourceCharList.index("ô", startSearchingIndex) # ô char means end of message, start searching from index zero of this mark 
            indexForMessageList = indexInCharSourceList - startSearchingIndex
            indexList.append(indexForMessageList)
          

        keyFile.close()
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
    indexWraplist = entireList[10_000:20_000] # get index wrap list from entire list of locationKeyList, indexWrapList and sourcharList
    indexListLength = len(indexList)
   
    for oneIndex in range(indexListLength): # go through index list and set index  wrapper
       
        indexList[oneIndex] += indexWraplist[oneIndex]
       
    return indexList


def createAllKeyListToFile(lengthOfKey, size):
    """
    Create location list for setting index to message
    and add index wrap list to the same list
    """
    
    locationList = []
    locationListCumSum = []
    locationListCumSum_b = []
    indexWrapList = []
    keyList=[]
    createdNumers = 0
    indexListLength = 10_000
    numberOfCharinFile = 0
    # sourceChatList
    sourceCharList= []
    # size in megabytes
    size = size* 1_024_000


    file = Path(filePathOfFile+"/keyFile.txt")
    result = file.is_file()

    if result:
        difference = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getctime(file))

        if difference.days < 30: # create new every month
            return # under 30 days old, do not create new one, return

    indexWrapList = np.random.choice( range(0, 100), indexListLength, replace=True).tolist() 


    while numberOfCharinFile < size:
            oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList()
            
            lengthOfOneLine = len(oneline)
            numberOfCharinFile += lengthOfOneLine
            sourceCharList.extend(oneline)
            oneline = ""

                                                                                                                                                                                                                                                                                                                                                
    with open(filePathOfFile+"/keyFile.txt", 'wb') as keyFile:
        #locationList = np.random.choice( range(0, 999999), lengthOfKey, replace=False).tolist() # creatue unique list on numbers (amount is lengthOfKey)
                                                                                                 # in range 0-999 999 (length of crypted message
        for i in range(lengthOfKey): 
            locationList.append(random.randrange(1,100))

        locationListCumSum = np.cumsum(locationList).tolist()
        random.shuffle(locationListCumSum) 

        
        keyList = locationListCumSum + indexWrapList
        keyList += sourceCharList
        pickle.dump(keyList, keyFile)
      
    keyFile.close()   

def loadLocationListFromFile():
    """
    Load location list when creating new message
    """

    locationList = []
    keyList = []
    
    file = Path(filePathOfFile+"/keyFile.txt")
    result = file.is_file()

    if result:

        with open (filePathOfFile+"/keyFile.txt", 'rb') as keyFile:
            keyList = pickle.load(keyFile)
            locationList = keyList[:20_000] # read location list from entire list(location + index wrap and source char list)
        keyFile.close()
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
            messageList.append(random.randrange(1,206)) # max. number is 206 because lenght of one character set is 106 and index wrap is max. 100
                                                        # together max 206 so all numbers is message must be between 1-206
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
    
    createAllKeyListToFile(10_000, 1)
    createMessageListToFile(1_000_000)
    writeFinalMessageFileByNumber()
    
def main():
    pass
    
if __name__ == "__main__":

    main()

