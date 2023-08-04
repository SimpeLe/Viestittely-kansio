import logging
import os
import pickle
 

def setLogger():
    numberOfHandledChar = 7
    logging.basicConfig(filename="loggingFile.txt",
    format='%(asctime)s %(message)s',
    filemode='w')
    
    logger = logging.getLogger()
    # Set the log of level to DEBUG
    logger.setLevel(logging.DEBUG)

def removeIndexFile():
    os.remove("indexFile.txt")

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
    logging.debug("loadListFromFile func start ")
    currentnList = []

    with open (filename, 'rb') as listFile:
        currentnList = pickle.load(listFile)

    logging.debug("currentnList length: %s", str(len(currentnList)))
    return currentnList


def findCharByIndexFromSourceCharFile():
     """
     Find characters from sourceCharFile and writes message
     """   

     sourceCharacterlineHandler  = ""
     charFoundByIndex = ""
     indexOfRowInCharFile = 0
     numberOfRowsInCharfile = 0
     numberOfHandledIndex = 0
     numberOfIndexHandle = 3 # search 3 index from each sorcecharacterRow
     indexrowflineHandled = False
     list = []
     list = readNumberFromfileToList("indexFile.txt")
     logging.debug("findCharByIndexFromSourceCharFile func start ")
     with open("Message.txt", 'w') as messageFile:
        with open("sourceCharacterFile.txt", 'r') as charFile:
            numberOfRowsInCharfile = len(charFile.readlines())
            logging.debug("numberOfRowsInCharfile: %s", str(numberOfRowsInCharfile))
            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
    
                if numberOfHandledIndex == numberOfIndexHandle: # find 3 index from one sourceCharFile row
                    #logging.debug("numberOfHandledIndex: %s", str(numberOfHandledIndex))
                    indexrowflineHandled = False
                    numberOfHandledIndex = 0
                    indexOfRowInCharFile +=1
                    if indexOfRowInCharFile == numberOfRowsInCharfile: # last row of file, start reading from zero
                        indexOfRowInCharFile = 0
                    charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    #logging.debug("indexOfRowInCharFile: %s", str(indexOfRowInCharFile))
                #if indexrowflineHandled == False:  # this refers to reading and handling one source Character row
                if numberOfHandledIndex < 3:
                    #logging.debug("index of row in char file: %s", str(indexOfRowInCharFile))
                    indexrowflineHandled = True
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

    messagelist = [] # read one row of message to this list
    locationlist = [] # read one location row to this list
    oneIndexRowlist = [] # write one index row to this list
    indexOfRowInMessageFile = 0
    indexOfrowInLocationInFile = 0
    numberOfMessageRowInFile = 0
    numberOfFoundLocation = 0
    indexFoundByLocation = 0
    locRow = ""
    locationCounter = 0 # count location together for finding rigth location from message row
    logging.debug("findIndexByLocationFromMessage func start ")
    messagelist = loadMessageListFromFile()
    logging.debug(" length: %s", str(len(messagelist)))
    locationlist = loadListFromFile("locationKeyFile.txt")
    logging.debug("oneLocationRowlist length: %s", str(len(locationlist)))
    with open("indexFile.txt", 'w') as indexFile:  

        for oneRowIndex in locationlist: # go through one location row and find location from messages
            if numberOfFoundLocation == 10: # 10 location are witten in one message row, load next message row 
                logging.debug("numberOfFoundLocation: %s", str(numberOfFoundLocation))
                numberOfFoundLocation = 0
            logging.debug("oneRowIndex: %s", str(oneRowIndex))
            locationCounter += oneRowIndex
            if oneRowIndex > len(locationlist)-1:
                    logging.debug("length oneLocationRowlist by index : %s", str(len(locationlist)-1))
                    logging.debug("length oneLocationRowlist out of range :")
                    break
            if locationCounter > len(messagelist)-1:
                    logging.debug("length oneMessageRowlist by index : %s", str(len(messagelist)-1))
                    logging.debug("length of locationCounter is bigger than message list  :")
                    break

            indexFoundByLocation = messagelist[locationCounter] # index by location from message row
            logging.debug("locationCounter: %s", str(locationCounter))
            logging.debug("oneRowIndex: %s", str(oneRowIndex))
            logging.debug("indexFoundByLocation: %s", str(indexFoundByLocation))
            oneIndexRowlist.append(indexFoundByLocation)
            if len(oneIndexRowlist) == 100: # when found enough index write to list
                logging.debug("write index line ")
                indexFile.write(','.join(str(i) for i in oneIndexRowlist))
                indexFile.write("\n")
                oneIndexRowlist.clear()
        
        # end of location numbers, write last index to file
        indexFile.write(','.join(str(i) for i in oneIndexRowlist))
        messagelist.clear() # end of location handling
        oneIndexRowlist.clear()
        locationlist.clear()
    
        indexFile.close()


def loadMessageListFromFile():
    """
    Load message to file
    """

    messageList = []

    with open ('messageKeyFile.txt', 'rb') as messageKeyFile:
        messageList = pickle.load(messageKeyFile)
    messageKeyFile.close()
    return messageList

def main():
    findIndexByLocationFromMessage()
    findCharByIndexFromSourceCharFile()

#setLogger()
#readNumberFromfileToList("locationTest.txt")
#readNumberFromfileToList(filename)
#findIndexByLocationFromMessage()
#findCharByIndexFromSourceCharFile()
#removeIndexFile()


if __name__ == "__main__":

    main()