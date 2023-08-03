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
    #print(filerowlen)
    #f.close()
    for line in range(0,filerowlen):
        listOfOneRow = [int(x) for x in lines[line].split(",")]
        entireNumeberList = entireNumeberList + listOfOneRow
    
    f.close()
    return entireNumeberList

def loadLocationListFromPickle():
    locationList = []

    with open ('locationKeyFileP.txt', 'rb') as locationKeyFile:
        locationList = pickle.load(locationKeyFile)

    print(locationList)
    return locationList


def findCharByIndexFromSourceCharFile():
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
     with open("testMessage.txt", 'w') as messageFile:
        with open("sourceCharacterFile.txt", 'r') as charFile:
            numberOfRowsInCharfile = len(charFile.readlines())
            logging.debug("numberOfRowsInCharfile: %s", str(numberOfRowsInCharfile))
            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
                #print(indexInLine)
                #print("index of numberOfHandledIndex 1 " + str(numberOfHandledIndex)+ "\n")
                if numberOfHandledIndex == numberOfIndexHandle: # find 3 index from one sourceCharFile row
                    logging.debug("numberOfHandledIndex: %s", str(numberOfHandledIndex))
                    print("set counters to zero\n")
                    indexrowflineHandled = False
                    numberOfHandledIndex = 0
                    indexOfRowInCharFile +=1
                    if indexOfRowInCharFile == numberOfRowsInCharfile: # last row of file, start reading from zero
                        indexOfRowInCharFile = 0
                    charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    logging.debug("indexOfRowInCharFile: %s", str(indexOfRowInCharFile))
                #if indexrowflineHandled == False:  # this refers to reading and handling one source Character row
                if numberOfHandledIndex < 3:
                    logging.debug("index of numberOfHandledIndex 1_2: %s", str(numberOfHandledIndex))
                    logging.debug("index of row in char file: %s", str(indexOfRowInCharFile))
                    indexrowflineHandled = True
                    logging.debug("handled index in loop %s", str(numberOfHandledIndex))
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine] # find one character from sourceCharFile row by index
                    logging.debug("charFoundByIndex in loop: %s", charFoundByIndex)
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
                        break
                    if charFoundByIndex == "è": # this is our own space mark in sourcharfile
                        charFoundByIndex = " "

                    elif charFoundByIndex == "á" or charFoundByIndex == "\v" or charFoundByIndex == "\r": # this is our own newline mark(á) in sourcharfile
                        charFoundByIndex = "\n"
                        
                    messageFile.write(charFoundByIndex)
                    numberOfHandledIndex +=1
                    print("index of numberOfHandledIndex 2 " + str(numberOfHandledIndex)+ "\n")
        list.clear()
        charFile.close()
     messageFile.close()

def findIndexByLocationFromMessage():
    oneMessageRowlist = [] # read one row of message to this list
    oneLocationRowlist = [] # read one location row to this list
    oneIndexRowlist = [] # write one index row to this list
    indexOfRowInMessageFile = 0
    indexOfrowInLocationInFile = 0
    numberOfMessageRowInFile = 0
    numberOfFoundLocation = 0
    indexFoundByLocation = 0
    locRow = ""
    locationCounter = 0 # count location together for finding rigth location from message row
    logging.debug("findIndexByLocationFromMessage func start ")
    with open("finalMessageByNumber.txt", 'r') as messageFile:
        with open("locationTest.txt", 'r') as locationFile:
            with open("indexFile.txt", 'w') as indexFile:
                messageRowLines = messageFile.readlines()
                print("messageFile file readed")
                numberOfMessageRowInFile = len(messageRowLines)
                logging.debug("numberOfIndexRowInFile: %s", str(numberOfMessageRowInFile))
                locationRowLines = locationFile.readlines()
                numberOfLocationRowInFile = len(locationRowLines)
                logging.debug("numberOfLocationRowInFile: %s", str(numberOfLocationRowInFile))
                messageFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                sourceMessagelineHandler = messageFile.readlines()[indexOfRowInMessageFile]

                oneMessageRowlist = [int(x) for x in messageRowLines[indexOfRowInMessageFile].split(",")] # read one message row to list
                print(oneMessageRowlist)
                
                for line in range(0, numberOfLocationRowInFile): # go throug  list of location 
                    logging.debug("line: %s", str(line))
                    if len(oneLocationRowlist) > 0:
                        oneLocationRowlist.clear() # clear list when reading next row
                    oneLocationRowlist = [int(x) for x in locationRowLines[line].split(",")] # read one location row to list
                    print(oneLocationRowlist)

                    for oneRowIndex in oneLocationRowlist: # oneLocationRowlist: # go through one location row and find location from messages
                        if numberOfFoundLocation == 10: # 10 location are witten in one message row, load next message row 
                            indexOfRowInMessageFile += 1
                            if indexOfRowInMessageFile < numberOfMessageRowInFile: # don't read out of index
                                oneMessageRowlist.clear() # clear list before reading new row
                                oneMessageRowlist = [int(x) for x in messageRowLines[indexOfRowInMessageFile].split(",")] # read one message row to list
                            numberOfFoundLocation = 0
                        logging.debug("oneRowIndex: %s", str(oneRowIndex))
                        locationCounter += oneRowIndex
                        logging.debug("locationCounter: %s", str(locationCounter))
                        indexFoundByLocation = oneMessageRowlist[locationCounter] # index by location from message row
                        print(indexFoundByLocation)
                        oneIndexRowlist.append(indexFoundByLocation)
                        if len(oneIndexRowlist) == 100: # when found enough index write to list
                            indexFile.write(','.join(str(i) for i in oneIndexRowlist))
                            indexFile.write("\n")
                            oneIndexRowlist.clear()
                        numberOfFoundLocation += 1
                    oneMessageRowlist.clear()
                # end of location numbers, write last index to file
                indexFile.write(','.join(str(i) for i in oneIndexRowlist))
                indexFile.write("\n")
                oneIndexRowlist.clear()
            
                indexFile.close()
            locationFile.close()
        messageFile.close()

filename = "indexFile.txt"
#readNumberFromfileToList("locationTest.txt")
#readNumberFromfileToList(filename)
#findIndexByLocationFromMessage()
#findCharByIndexFromSourceCharFile()
#removeIndexFile()
loadLocationListFromPickle()