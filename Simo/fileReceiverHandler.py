import logging
import os
import pickle
from pathlib import Path


def setLogger():
    
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='a')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)


def offerMessageToUI():
    with open("Message.txt", 'r') as messageFile:

        message = messageFile.read()
        messageFile.close()
        os.remove("Message.txt") # delete message after it has been returned to UI
        logging.debug("message to ui : %s", message)
        return message

def getPathFromUI(path):
    global filePathOfFile 
    #filePathOfFile = "C:/Users/Ville/project/Viestittely-kansio/source" 
    filePathOfFile = path
    logging.debug("filePathOfFile receiverHandler: %s", filePathOfFile)
    print(filePathOfFile)


def loadListFromFile(filename):
    logging.debug("loadListFromFile func start")
    realPath = filePathOfFile+filename
    file = Path(filePathOfFile+filename)
    result = file.is_file()

    if not result:
         print("File not found")
         return

    currentnList = []
    realPath =  filePathOfFile+filename
    print("realPath")

    with open (realPath, 'rb') as listFile:
        currentnList = pickle.load(listFile)

    logging.debug("currentnList length: %s", str(len(currentnList)))
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
         #print("File found")
         h = 8
     else:
        print("no sourcecharfile")
        return
     
     logging.debug("findCharByIndexFromSourceCharFile func start again ")
     with open("Message.txt", 'w') as messageFile:
         realPath =  filePathOfFile+ "/sourceCharacterFile.txt"
         with open(realPath, 'r') as charFile:
            list = findIndexByLocationFromMessage()
            logging.debug("index list when receiving in loop: %s", list)
            logging.debug("index list length when receiving in loop: %s", len(list))
            numberOfRowsInCharfile = len(charFile.readlines())
            logging.debug("numberOfRowsInCharfile: %s", str(numberOfRowsInCharfile))
            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
                logging.debug("indexInLine when receiving in loop: %s", indexInLine)
                if numberOfHandledIndex == numberOfIndexHandle: # find 3 index from one sourceCharFile row
                    #logging.debug("numberOfHandledIndex: %s", str(numberOfHandledIndex))
                    logging.debug("test 1")
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    logging.debug("charFoundByIndex after 3 index 1: %s", charFoundByIndex)
                    if charFoundByIndex == "ô": #  end of message, close file
                        logging.debug("end of message reading when receive before loading new sourceChar row")
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
                    logging.debug("indexOfRowInCharFile when re4ceiving: %s", str(indexOfRowInCharFile))


                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    logging.debug("charFoundByIndex after 3 index 2: %s", charFoundByIndex)
                    if charFoundByIndex == "ô": #  end of message, close file
                        logging.debug("end of message reading when receive after loading new sourceChar row")
                        messageFile.close()
                        list.clear()
                        charFile.close()
                        break

                    # if charFoundByIndex == "ô": #  end of message, close file
                    #     logging.debug("end of message reading when receive after loading new sourceChar row")
                    #     messageFile.close()
                    #     list.clear()
                    #     charFile.close()
                    #     break
                
                if numberOfHandledIndex < 3:
                    #logging.debug("index of row in char file: %s", str(indexOfRowInCharFile))
                    logging.debug("handled index when receiving in loop %s", str(numberOfHandledIndex))
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    logging.debug("charFoundByIndex when receiving in loop: %s", charFoundByIndex)
                    if charFoundByIndex == "ô": #  end of message, close file
                        logging.debug("end of message reading when receive")
                        logging.debug("Index list when receiving in loop: %s", list)
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
    logging.debug("findIndexByLocationFromMessage func start ")
    messagelist = loadMessageListFromFile()
    logging.debug(" length: %s", str(len(messagelist)))
    locationlist = loadListFromFile("/locationKeyFile.txt")
    logging.debug("oneLocationRowlist length: %s", str(len(locationlist)))
    
    for oneLocation in locationlist: # go through  location list and find index by location from messages
        logging.debug("oneLocation: %s", str(oneLocation))
        indexFoundByLocation = messagelist[oneLocation] # index by location from message list
        logging.debug("indexFoundByLocation: %s", str(indexFoundByLocation))
        indexList.append(indexFoundByLocation)
        
    messagelist.clear() # end of location handling
    locationlist.clear()
    return indexList
        

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
    #findIndexByLocationFromMessage()
    setLogger()
   # getPathFromUI("sdtgh")
    findCharByIndexFromSourceCharFile()

#setLogger()
#findIndexByLocationFromMessage()
#findCharByIndexFromSourceCharFile()


if __name__ == "__main__":

    main()