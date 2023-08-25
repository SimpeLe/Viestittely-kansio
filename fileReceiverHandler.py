import os
import pickle
from pathlib import Path


def offerMessageToUI():
    """
    Return message to UI after it has been decrypted
    
    """
    file = Path("Message.txt")
    
    result = file.is_file()
    if not result:
            return #no message file

    with open("Message.txt", 'r') as messageFile:
        
        message = messageFile.read()
        messageFile.close()
        os.remove("Message.txt") # delete message after it has been returned to UI
        return message

def getPathFromUI(path):
    global filePathOfFile 
    filePathOfFile = path


def loadListFromFile(filename):
    realPath = filePathOfFile+filename
    file = Path(filePathOfFile+filename)
    result = file.is_file()

    if not result:
         return #File not found

    currentnList = []
    realPath =  filePathOfFile+filename

    with open (realPath, 'rb') as listFile:
        currentnList = pickle.load(listFile)

    return currentnList


def findCharByIndexFromSourceCharFile():
     """
     Find characters from sourceCharFile and writes message
     """   

     sourceCharacterlineHandler  = "" # read one row of source char 
     charFoundByIndex = ""
     indexOfRowInCharFile = 0
     numberOfRowsInCharfile = 0
     numberOfHandledIndex = 0
     numberOfIndexHandle = 3 # search 3 index from each sorcecharacterRow
     list = [] # load index list here

     realPath = ""
     file = Path(filePathOfFile+"/sourceCharacterFile.txt")
     result = file.is_file()

     if result:
         h = 8
     else:
        return #no sourcecharfile
     
     messageExist = False
     messageExist = checkIfMessageExist()
     if messageExist:
        logging.debug("there is message")
     else:
        return #no message: return
     
     with open("Message.txt", 'w') as messageFile:
         realPath =  filePathOfFile+ "/sourceCharacterFile.txt"
         with open(realPath, 'r') as charFile:
            list = findIndexByLocationFromMessage()
            numberOfRowsInCharfile = len(charFile.readlines())
            charFile.seek(0) #  set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
                
                if numberOfHandledIndex == numberOfIndexHandle: # find 3 index from one sourceCharFile row
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
                        list.clear()
                        charFile.close()
                        break

                    numberOfHandledIndex = 0
                    indexOfRowInCharFile +=1
                    if indexOfRowInCharFile == numberOfRowsInCharfile: # last row of file, start reading from zero
                        indexOfRowInCharFile = 0
                    charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    

                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
                        list.clear()
                        charFile.close()
                        break
                
                if numberOfHandledIndex < 3:
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
                        list.clear()
                        charFile.close()
                        break
                    if charFoundByIndex == "è": # this is our own space mark in sourcharfile
                        charFoundByIndex = " "

                    elif charFoundByIndex == "á" or charFoundByIndex == "\v" or charFoundByIndex == "\r": # this is our own newline mark(á) in sourcharfile
                        charFoundByIndex = "\n"
                        
                    messageFile.write(charFoundByIndex)
                    numberOfHandledIndex +=1
    
         list.clear()
         charFile.close()
     messageFile.close()

def findIndexByLocationFromMessage():
    """
    Searches index from message based on location
    """

    messagelist = [] # read list of message here
    locationlist = [] # read list of location 
    indexList = [] # save founded index here and return list
    indexFoundByLocation = 0
    messageExist = False
    messageExist = checkIfMessageExist()
    if messageExist:
        messagelist = loadMessageListFromFile()
    else:
        return #no message
    
    locationlist = loadListFromFile("/locationKeyFile.txt")
    locationlist = locationlist[:10_000] # separate location list from index wrap list
    
    
    for oneLocation in locationlist: # go through  location list and find index by location from messages
        indexFoundByLocation = messagelist[oneLocation] # index by location from message list
        indexList.append(indexFoundByLocation)
        
    messagelist.clear() # end of location handling
    locationlist.clear()
    indexList = removeIndexWrap(indexList)
    removeMessageFile() # remove message
    return indexList

def removeMessageFile():

    filename = "/messageFile.txt"
    realPath = filePathOfFile+filename

    file = Path(realPath)
    result = file.is_file()
    if result:
        os.remove(realPath) # delete message file 

def removeIndexWrap(indexList):
    entireList = []
    indexWraplist = []
    wrappedIndex = 0
    counter = 0
    indexListLength = 0
    entireList = loadListFromFile("/locationKeyFile.txt")
    indexWraplist = entireList[10_000:] # get index wrap list from entire list of locationKeyList and indexWrapList
    indexListLength = len(indexList)

    for oneIndex in range(indexListLength): # go through index list and remove index  wrapper
        
        indexList[oneIndex] -= indexWraplist[oneIndex]

    return indexList
        
def checkIfMessageExist():
    """
    Check if messageFile.txt file exist, if not exist do not to start handle message
    """
    
    filename = "/messageFile.txt"
    realPath = filePathOfFile+filename
    file = Path(filePathOfFile+filename)
    result = file.is_file()
    if not result:
        #no file in selected folder
        file = Path(filename)
        result = file.is_file()
        if result:
            return True #file in home folder
        else:  
            return False #no file in home folder
    else:
        logging.debug("file messagefile.txt in selected folder")
        return True



def loadMessageListFromFile():
    """
    Load message to file
    """

    file = Path(filePathOfFile+"/messageFile.txt")
    result = file.is_file()
     
    messageList = []
    filename = "/messageFile.txt"
    realPath = filePathOfFile+filename
    file = Path(filePathOfFile+filename)
    result = file.is_file()

    if result:
         with open (realPath, 'rb') as messageKeyFile:
            messageList = pickle.load(messageKeyFile)
    else:
        with open ('messageFile.txt', 'rb') as messageKeyFile:
            messageList = pickle.load(messageKeyFile)

    messageKeyFile.close()
    return messageList

def main():
    pass



if __name__ == "__main__":

    main()