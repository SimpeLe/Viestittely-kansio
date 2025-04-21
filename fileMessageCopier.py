import random
import pickle
import logging
from pathlib import Path
import shutil
import os


def copyOneMessageToList(targetPath, sourcePath):
    """
    Copy message to group of messages
    """

    targetList = [] # existing list of messages
    sourceList = [] # message to copy
    locationList = []
    i = 0
    targetName = ""
    sourceName = ""
    targetIndex = 0
    sourceIndex = 0

    locationListLength = 0
    targetListLength = 0
    sourcelistLength = 0
     
   
    targetMessages = Path(targetPath+"/messageFile.txt") 
    targetExist = targetMessages.is_file()
    sourceMessage = Path(sourcePath+"/messageFile.txt")
    sourceExist = sourceMessage.is_file()


    locationListFile = Path(sourcePath+"/locationFile.txt")
    locationFileExist = locationListFile.is_file()


    if not locationFileExist:
        return # no location list, return


    if not sourceExist:
        return #no source file, return

    if targetExist:
        with open (sourceMessage, 'rb') as sourceMessageFile: # open message file to copy new message 
            sourceList = pickle.load(sourceMessageFile)
        sourceMessageFile.close()
        sourcelistLength = len(sourceList)
        

        with open(targetMessages, 'rb') as targetFile: # open existing list of messages
            targetList = pickle.load(targetFile)
            targetListLength = len(targetList)
            
            targetFile.close()
            with open (locationListFile, 'rb') as locationFile: # open location file
                 locationList = pickle.load(locationFile)
                 locationListLength = len(locationList)
                
                 for i in range(locationListLength):
                     
                     targetIndex = targetList[locationList[i]]
                     sourceIndex = sourceList[locationList[i]]

                     targetList[locationList[i]] = sourceList[locationList[i]] # copy index by location to new file
                     targetIndex = targetList[locationList[i]]
            
            with open(targetMessages, 'wb') as targetFile:
                pickle.dump(targetList, targetFile)

        targetListLength = len(targetList)
        targetFile.close()
        locationFile.close()
        sourceMessageFile.close()
        sourceList.clear()
        targetList.clear()
        locationList.clear()

        
    else:
        logging.debug("target does not exist")
        file = Path(sourcePath+"/messageFile.txt")
        sourceName = sourcePath+"/messageFile.txt"
        result = file.is_file()
        if result:
            print("just rename file")
            logging.debug("just rename file")
            if  targetPath == sourcePath:
                h = 6
            else:
                with open (sourceMessage, 'rb') as messageFile: # open one message
                    sourceList = pickle.load(messageFile)
                messageFile.close()
                os.rename(sourcePath+'/messageFile.txt', sourcePath+'/Messages.txt')
                shutil.copyfile(sourcePath+"/Messages.txt", targetPath+"/Messages.txt")
     

def retrieveCopy(targetPath, sourcePath):
    """"
    Find message from group of messages
    """
    
    messageList = []
    copyId = []
    oneMessage = []

        
    messageId   = Path(targetPath+"/copyIdentifier.txt")
    targetExist = messageId.is_file()
    fileMessages = Path(sourcePath+"/Messages.txt")
    sourceExist = fileMessages.is_file()


    if not sourceExist:
        return # no source file from retrieve, return

    with open (sourcePath+'/Messages.txt', 'rb') as copyFile:
        messageList = pickle.load(copyFile)
    copyFile.close()

    if not targetExist:
        return # no id file from retrieve, return


    with open (targetPath+"/copyIdentifier.txt", 'rb') as idFile:
        copyId = pickle.load(idFile)
    idFile.close()
    
    area = len(messageList)//1_000_000
    i = 0
    origlistLength = 1_000_000 # length of one message
    while i<area:
        if copyId[0] == messageList[origlistLength*i] and copyId[1] == messageList[origlistLength*i+1] and copyId[2] == messageList[origlistLength*i+2] \
        and copyId[3] == messageList[origlistLength*i+3] and copyId[4] == messageList[origlistLength*i+4] and  copyId[5] == messageList[origlistLength*i+100]:
            oneMessage = messageList[origlistLength*i:origlistLength*i+1_000_000]
            break
        i +=1


    if  targetPath != sourcePath:
        with open (targetPath+'/messageFile.txt', 'wb') as messageFile:
             pickle.dump(oneMessage, messageFile)
        messageFile.close()

    messageList.clear()
    oneMessage.clear()

    

