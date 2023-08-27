import random
import pickle
import logging
from pathlib import Path
import shutil
import os

def setLogger():
    
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='w')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)


def copyOneMessageToList(targetPath, sourcePath):

    logging.debug("copyOneMessageToList func start")
    logging.debug("targetPath : %s", str(targetPath))
    logging.debug("sourcePath : %s", str(sourcePath))


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
        logging.debug("no sorce file, return")
        return

    logging.debug("fileMessages : %s", str(fileMessages))
    if targetExist:
        print("source and target Exist")
        logging.debug("source and target Exist")
        with open (oneMessage, 'rb') as messageFile: # open one message to add list
            copyList = pickle.load(messageFile)
        messageFile.close()


        logging.debug("fileMessages : %s", str(fileMessages))
        with open(fileMessages, 'rb+') as copyFile: # open existing list of messages
            logging.debug("add to list next")
            targetList = pickle.load(copyFile)
            targetList += copyList # add message to list
            pickle.dump(targetList, copyFile)
        copyFile.close()
        
    else:
        logging.debug("no messages yet")
        file = Path(sourcePath+"/messageFile.txt")
        sourceName = sourcePath+"/messageFile.txt"
        result = file.is_file()
        if result:
            print("just rename file")
            if  targetPath == sourcePath:
                print("same path")
                logging.debug("same path")
            
            else:
        
                logging.debug("make first copy, just rename")
                logging.debug("create copylist")
                with open (oneMessage, 'rb') as messageFile: # open one message
                    copyList = pickle.load(messageFile)
                messageFile.close()
                

                os.rename(sourcePath+'/messageFile.txt', sourcePath+'/Messages.txt')
                logging.debug("sourcePath : %s", str(sourcePath))
                logging.debug("targetPath : %s", str(targetPath))
                shutil.copyfile(sourcePath+"/Messages.txt", targetPath+"/Messages.txt")
     

    while i<5: # create id for copied file
        messageId[i] =  copyList[i]  
        i +=1

    messageId[5] =  copyList[100] 

    if  targetPath != sourcePath:
        logging.debug("create copyId file")
        with open(targetPath+"/copyIdentifier.txt", 'wb') as idFile:
            pickle.dump(messageId, idFile)
        idFile.close()

   

def retrieveCopy(targetPath, sourcePath):

    logging.debug("retrieveCopy func start")
    logging.debug("targetPath retrieve: %s", str(targetPath))
    logging.debug("sourcePath retrieve: %s", str(sourcePath))

    messageList = []
    copyId = []
    oneMessage = []

        
    messageId   = Path(targetPath+"/copyIdentifier.txt")
    targetExist = messageId.is_file()
    fileMessages = Path(sourcePath+"/Messages.txt")
    sourceExist = fileMessages.is_file()

    logging.debug("sourcePath fileMessages: %s", str(fileMessages))

    if not sourceExist:
        print("no source file from retrieve, return")
        logging.debug("no source file from retrieve, return")
        return


    with open (sourcePath+'/Messages.txt', 'rb') as copyFile:
        messageList = pickle.load(copyFile)
    copyFile.close()

    if not targetExist:
        print("no id  file from retrieve, return")
        logging.debug("no id file from retrieve, return")
        return


    with open (targetPath+"/copyIdentifier.txt", 'rb') as idFile:
        copyId = pickle.load(idFile)
    idFile.close()
    
    area = len(messageList)//1_000_000
    i = 0
    origlistLength = 1_000_000 # length of one message
    while i<area:
        print(str(i))
        print(str(copyId[0]))
        print(str(messageList[origlistLength*i]))
        if copyId[0] == messageList[origlistLength*i] and copyId[1] == messageList[origlistLength*i+1] and copyId[2] == messageList[origlistLength*i+2] \
        and copyId[3] == messageList[origlistLength*i+3] and copyId[4] == messageList[origlistLength*i+4] and  copyId[5] == messageList[origlistLength*i+100]:
            print("found")
            print(str(i))
            oneMessage = messageList[origlistLength*i:origlistLength*i+1_000_000]
            break
        i +=1


    if  targetPath != sourcePath:
        logging.debug("write message  to target")
        with open (targetPath+'/messageFile.txt', 'wb') as messageFile:
             pickle.dump(oneMessage, messageFile)
        messageFile.close()


    messageList.clear()
    oneMessage.clear()

    

