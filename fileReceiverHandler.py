import os
import pickle
from pathlib import Path
import fileMessageHandler as send
import random


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
     Find characters from sourceCharList and writes message
     """   
     
     charFoundByIndex = ""
     list = [] # load index list here
     entireList=[]
     sourceCharList =[]
     startSearchingIndex = 0 # start index to search each character from char list
     realIndex = 0 # Real index in source character list

     realPath = ""
     file = Path(filePathOfFile+"/keyFile.txt")
     result = file.is_file()

     if not result:
         return #no sourcecharfile
        
     
     messageExist = False
     messageExist = checkIfMessageExist()
     if not messageExist:
        return #there is not message
     
     with open("Message.txt", 'w') as messageFile:
         realPath = filePathOfFile+ "/keyFile.txt"
         with open(realPath, 'rb') as keyFile:
            entireList = pickle.load(keyFile)
            sourceCharList = entireList[20_006:]
            list = findIndexByLocationFromMessage()

            for indexInLine in list: # go through entire index list
                
                realIndex += startSearchingIndex + indexInLine
                charFoundByIndex = sourceCharList[realIndex]
              
                if charFoundByIndex == "è": # this is our own space mark in sourcharfile
                    charFoundByIndex = " "

                elif charFoundByIndex == "á" or charFoundByIndex == "\v" or charFoundByIndex == "\r": # this is our own newline mark(á) in sourcharfile
                    charFoundByIndex = "\n"

                if not charFoundByIndex == "ô": # do not write end mark to message
                    messageFile.write(charFoundByIndex)

                if charFoundByIndex == "ô": #  end of message, close file
                    messageFile.close()
                    list.clear()
                    keyFile.close()
                    break

                startSearchingIndex += len (send.createOneSourceCharacterList()) # increase start searching point for each character
                realIndex = 0
                    
         list.clear()
         keyFile.close()
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
    
    locationlist = loadListFromFile("/keyFile.txt")
    locationlist = locationlist[:10_003] # separate location list from index wrap list

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
    indexListLength = 0
    indexRandWraplist = []
    randomizedIndexWrapList = []
    

    entireList = loadListFromFile("/keyFile.txt")

    indexRandWraplist = entireList[10_003:10_006] # random number new 8.12
    
    indexRandWraplist = entireList[10_003:10_006]
    indexWraplist = entireList[10_006:20_006] # get index wrap list from entire list of locationKeyList and indexWrapList

    randomizedIndexWrapList = randomizeIndexWrapList(indexRandWraplist, indexWraplist, indexList)
   
    indexListLength = len(indexList)

    for oneIndex in range(indexListLength): #(indexListLength): # go through index list and remove index  wrapper
        
        indexList[oneIndex] -= randomizedIndexWrapList[oneIndex] 
   

    indexList = indexList[3:] # remove rand number from index list

    return indexList  


def randomizeIndexWrapList(indexRandWraplist, indexWrapList, indexList ):
    
    randomizedList = []
    storageList = []
    storageListSec = []
    randomNumber = 0
    firstRandomnumber = 0
    secondRandomnumber = 0
    thirdRandomnumber = 0
   
    
    firstRandomnumber = indexList[0] - indexRandWraplist[0]
    secondRandomnumber = indexList[1] - indexRandWraplist[1]
    thirdRandomnumber = indexList[2] - indexRandWraplist[2]

    
    if firstRandomnumber == 0 and secondRandomnumber == 0:
        randomNumber = thirdRandomnumber
    if firstRandomnumber == 0 and secondRandomnumber > 0:
       randomNumber = int(str(secondRandomnumber) + str(thirdRandomnumber))
    if firstRandomnumber > 0:
        randomNumber = int(str(firstRandomnumber) + str(secondRandomnumber) + str(thirdRandomnumber))
   
    storageList = indexWrapList[randomNumber:]
    storageListSec = indexWrapList[:randomNumber]
 
    randomizedList.append(indexRandWraplist[0])
    randomizedList.append(indexRandWraplist[1])
    randomizedList.append(indexRandWraplist[2])

    randomizedList += storageList + storageListSec
    
    return randomizedList
        
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
        return True #file messagefile.txt in selected folder



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