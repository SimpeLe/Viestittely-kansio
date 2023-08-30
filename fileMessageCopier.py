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
    copyList = [] # message to copy
    messageId = [0,0,0,0,0,0,0]
    i = 0
    targetName = ""
    sourceName = ""
     
    fileMessages = Path(targetPath+"/Messages.txt")
    targetExist = fileMessages.is_file()
    oneMessage = Path(sourcePath+"/messageFile.txt")
    sourceExist = oneMessage.is_file()


    if not sourceExist:
        return #no sorce file, return

    if targetExist:
        with open (oneMessage, 'rb') as messageFile: # open one message to add list
            copyList = pickle.load(messageFile)
        messageFile.close()

        with open(fileMessages, 'rb+') as copyFile: # open existing list of messages
            targetList = pickle.load(copyFile)
            targetList += copyList # add message to list
            pickle.dump(targetList, copyFile)
        copyFile.close()
        
    else:
        file = Path(sourcePath+"/messageFile.txt")
        sourceName = sourcePath+"/messageFile.txt"
        result = file.is_file()
        if result:
            print("just rename file")
            if  targetPath == sourcePath:
                h = 6
            else:
                with open (oneMessage, 'rb') as messageFile: # open one message
                    copyList = pickle.load(messageFile)
                messageFile.close()
                os.rename(sourcePath+'/messageFile.txt', sourcePath+'/Messages.txt')
                shutil.copyfile(sourcePath+"/Messages.txt", targetPath+"/Messages.txt")
     

    while i<5: # create id for copied file
        messageId[i] =  copyList[i]  
        i +=1

    messageId[5] =  copyList[100] 

    if  targetPath != sourcePath:
        with open(targetPath+"/copyIdentifier.txt", 'wb') as idFile:
            pickle.dump(messageId, idFile)
        idFile.close()

   

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

    

