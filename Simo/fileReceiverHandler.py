import logging
import os
import pickle
from pathlib import Path


def setLogger():
    
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='w')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)


def offerMessageToUI():
    with open("messageFile.txt", 'r') as messageFile:
        message = messageFile.read()
        messageFile.close()
        os.remove("messageFile.txt") # delete message after it has been returned to UI
        return message

def getPathFromUI(path):
    global filePathOfFile 
    filePathOfFile = path
    logging.debug("filePathOfFile : %s", filePathOfFile)
    print(filePathOfFile)


def readNumberFromfileToList(filename):
    logging.debug("readNumberFromfileToList func start ")
     
    listOfOneRow=[]
    entireNumeberList=[]
    f = open(filename,"r")
    lines = f.readlines()
    f.seek(0)
    filerowlen = len(f.readlines())
    
    for line in range(0,filerowlen):
        listOfOneRow = [int(x) for x in lines[line].split(",")]
        entireNumeberList = entireNumeberList + listOfOneRow
    
    f.close()
    return entireNumeberList

def loadListFromFile(filename):
    logging.debug("loadListFromFile func start")
    realPath = filePathOfFile+filename
    file = Path(filePathOfFile+filename)
    result = file.is_file()

    if result:
         print("File found")
    else:
        print("no file")
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
     
     logging.debug("findCharByIndexFromSourceCharFile func start ")
     with open("messageFile.txt", 'w') as messageFile:
         realPath =  filePathOfFile+ "/sourceCharacterFile.txt"
         with open(realPath, 'r') as charFile:
            list = findIndexByLocationFromMessage()
            numberOfRowsInCharfile = len(charFile.readlines())
            logging.debug("numberOfRowsInCharfile: %s", str(numberOfRowsInCharfile))
            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
    
                if numberOfHandledIndex == numberOfIndexHandle: # find 3 index from one sourceCharFile row
                    #logging.debug("numberOfHandledIndex: %s", str(numberOfHandledIndex))
                    numberOfHandledIndex = 0
                    indexOfRowInCharFile +=1
                    if indexOfRowInCharFile == numberOfRowsInCharfile: # last row of file, start reading from zero
                        indexOfRowInCharFile = 0
                    charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    #logging.debug("indexOfRowInCharFile: %s", str(indexOfRowInCharFile))
                
                if numberOfHandledIndex < 3:
                    #logging.debug("index of row in char file: %s", str(indexOfRowInCharFile))
                    #logging.debug("handled index in loop %s", str(numberOfHandledIndex))
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    #logging.debug("charFoundByIndex in loop: %s", charFoundByIndex)
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
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
        indexFoundByLocation = messagelist[oneLocation] # index by location from message row
        logging.debug("oneLocation: %s", str(oneLocation))
        logging.debug("indexFoundByLocation: %s", str(indexFoundByLocation))
        indexList.append(indexFoundByLocation)
        
    messagelist.clear() # end of location handling
    locationlist.clear()
    return indexList
        

def loadMessageListFromFile():
    """
    Load message to file
    """

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
    #setLogger()
    getPathFromUI("sdtgh")
    findCharByIndexFromSourceCharFile()

#setLogger()
#readNumberFromfileToList(filename)
#findIndexByLocationFromMessage()
#findCharByIndexFromSourceCharFile()
#removeIndexFile()


if __name__ == "__main__":

    main()