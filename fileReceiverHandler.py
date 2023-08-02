


def removeLocationKey():
    tre  = 7

def readNumberFromfileToList(filename):
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
        #list2 = [int(x) for x in lines[1].split(",")]
        entireNumeberList = entireNumeberList + listOfOneRow
        #print(entireNumeberList)
    return entireNumeberList

def findIndexFromSourceCharFile():
    sourceCharacterlineHandler  = ""
    indexlineHandler = []
    charFoundByIndex = ""
    indexOfRowInCharFile = 0
    numberOfindexHandle = 3 # search 3 index from each sorcecharacterRow
    numberOfHandledIndex = 0
    messagelineHandler = "" # contains one line of original message
    messageRowLength = 0 # length of message line
    numberOfIndexHandle = 3 # search 3 index from each sorcecharacterRow
    lineHandled = False
    messageLentghCounter = 0
    indexrowrofile = ""
    indexrowflineHandled = False

    with open("indexFile.txt", 'r') as indexFile:
        with open("testOrigMessage.txt", 'w') as messageFile:
            with open("sourceCharacterFile.txt", 'r') as charFile:
            
                for readline in indexFile: # go through hole file line by line
                    print("print readline\n")
                    print (readline)
                    #indexlineHandler =  readline[:-1] # one row of index, remove newline
                    indexlineHandler = [int(number) for number in indexFile.readline().split(',')] # read one row of index to list
                    
                #   line_strip = messageFile.readline() #.strip()
                    print(indexlineHandler)
                    #newline_break += line_strip
                #   print(newline_break)
                
                    for indexInLine in indexlineHandler:
                        print("handled index in loop " + str(numberOfHandledIndex) +"\n")
                        if numberOfHandledIndex == numberOfIndexHandle: # 3
                            print("set counters to zero\n")
                            lineHandled = False
                            numberOfHandledIndex = 0
                            indexOfRowInCharFile +=1
                            startSearchingIndex = 0
                        if lineHandled == False:  # this refers to reading and handling one source Character row
                            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                            print("index of row in char file " + str(indexOfRowInCharFile)+ "\n")
                            #print(indexOfRowInCharFile)
                            lineHandled = True
                            #sourceCharacterlineHandler = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
                            # sourceCharacterlineHandler = charFile.readline()[0]
                        print("handled index in loop " + str(numberOfHandledIndex) +"\n")
                        charFoundByIndex = sourceCharacterlineHandler.index(indexInLine)
                        print("charFoundByIndex in loop " + charFoundByIndex +"\n")
                        if charFoundByIndex == "ô": #  end of message, close file
                            messageFile.close()
                        if charFoundByIndex == "è":
                            charFoundByIndex = " "

                        elif charFoundByIndex == "á" or charFoundByIndex == "\v" or charFoundByIndex == "\r":
                            charFoundByIndex = "\n"
                            
                        messageFile.write(charFoundByIndex)
                        


                                              
                        if numberOfHandledIndex == 0:
                            #indexInCryptedMessage = indexInCharSourceLine
                            #indexrowrofile += str(indexInCharSourceLine)+","
                            startSearchingIndex = 100
                        elif numberOfHandledIndex == 1: # set startseachindex for second index in row of sourcecharFile
                            startSearchingIndex = 200
                            #indexCounter = (100 - indexInCryptedMessage) + (indexInCharSourceLine - 100)
                            #indexInCryptedMessage = indexCounter
                            #indexrowrofile += str(indexInCharSourceLine)+","
                        elif numberOfHandledIndex == 2: # set startseachindex for third index in row of sourcecharFile
                            startSearchingIndex = 200
                            #indexCounter = (200 - indexInCryptedMessage) + (indexInCharSourceLine - 200)
                            #indexInCryptedMessage = indexCounter
                            #indexrowrofile += str(indexInCharS
                        numberOfHandledIndex +=1


def testfindCharByIndexFromSourceCharFile():
     sourceCharacterlineHandler  = ""
     charFoundByIndex = ""
     indexOfRowInCharFile = 0
     numberOfHandledIndex = 0
     numberOfIndexHandle = 3 # search 3 index from each sorcecharacterRow
     indexrowflineHandled = False
     list = []
     list = readNumberFromfileToList("indexFile.txt")
     with open("testMessage.txt", 'w') as messageFile:
        with open("sourceCharacterFile.txt", 'r') as charFile:
            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            for indexInLine in list: # go through entire index list
                #print(indexInLine)
                #print("index of numberOfHandledIndex 1 " + str(numberOfHandledIndex)+ "\n")
                if numberOfHandledIndex == numberOfIndexHandle: # 3
                    print("index of numberOfHandledIndex 1 " + str(numberOfHandledIndex)+ "\n")
                    print("set counters to zero\n")
                    indexrowflineHandled = False
                    numberOfHandledIndex = 0
                    indexOfRowInCharFile +=1
                    charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    print("index of row in char file " + str(indexOfRowInCharFile)+ "\n")
                #if indexrowflineHandled == False:  # this refers to reading and handling one source Character row
                if numberOfHandledIndex < 3:
                    print("index of numberOfHandledIndex 1_2 " + str(numberOfHandledIndex)+ "\n")
                    #charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    #sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                    print("index of row in char file " + str(indexOfRowInCharFile)+ "\n")
                    #print(indexOfRowInCharFile)
                    indexrowflineHandled = True
                    #sourceCharacterlineHandler = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
                    # sourceCharacterlineHandler = charFile.readline()[0]
                    print("handled index in loop " + str(numberOfHandledIndex) +"\n")
                    charFoundByIndex = sourceCharacterlineHandler[indexInLine]
                    print("charFoundByIndex in loop " + charFoundByIndex +"\n")
                    if charFoundByIndex == "ô": #  end of message, close file
                        messageFile.close()
                        break
                    if charFoundByIndex == "è":
                        charFoundByIndex = " "

                    elif charFoundByIndex == "á" or charFoundByIndex == "\v" or charFoundByIndex == "\r":
                        charFoundByIndex = "\n"
                        
                    messageFile.write(charFoundByIndex)
                    numberOfHandledIndex +=1
                    print("index of numberOfHandledIndex 2 " + str(numberOfHandledIndex)+ "\n")
        charFile.close()
     messageFile.close()

def findLocationFromMessage():
    oneMessageRowlist = [] # read one row of message to this list
    oneLocationRowlist = [] # read one location row to this list
    oneIndexRowlist = []
    indexOfRowInMessageFile = 0
    indexOfrowInLocationInFile = 0
    numberOfMessageRowInFile = 0
    numberOfFoundLocation = 0
    indexFoundByLocation = 0
    locationCounter = 0 # count location together for finding rigth location from message row
    with open("finalMessage.txt", 'r') as messageFile:
        with open("locationTest.txt", 'r') as locationFile:
            with open("indexTest.txt", 'w') as indexFile:
                messageRowLines = messageFile.readlines()
                print("messageFile file readed")
                numberOfMessageRowInFile = len(messageRowLines)
                print("numberOfIndexRowInFile " + str(numberOfMessageRowInFile) +"\n")
                locationRowLines = locationFile.readlines()
                numberOfLocationRowInFile = len(locationRowLines)
                print("numberOfLocationRowInFile " + str(numberOfLocationRowInFile) +"\n")
                messageFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                sourceMessagelineHandler = messageFile.readlines()[indexOfRowInMessageFile]

                oneMessageRowlist = [int(x) for x in messageRowLines[indexOfRowInMessageFile].split(",")] # read one message row to list
                print(oneMessageRowlist)
                
                for line in range(0, numberOfLocationRowInFile): # go throug all list of location 
                    listOfOneRowLocation = [int(x) for x in locationRowLines[line].split(",")] # read one location row to list
                    print(listOfOneRowLocation)

                    for oneRowIndex in listOfOneRowLocation: # go through one location row and find location from messages
                        if numberOfFoundLocation == 10: # 10 location are witten in one message row
                            indexOfRowInMessageFile += 1
                            oneMessageRowlist = [int(x) for x in messageRowLines[indexOfRowInMessageFile].split(",")] # read one message row to list
                            numberOfFoundLocation = 0

                        print("oneRowIndex " + str(oneRowIndex)+ "\n")
                        locationCounter += oneRowIndex
                        print("locationCounter " + str(locationCounter)+ "\n")
                        indexFoundByLocation = oneMessageRowlist[locationCounter] # index by location from message row
                        print(indexFoundByLocation)
                        oneIndexRowlist.append(indexFoundByLocation)
                        if len(oneIndexRowlist) == 100: # when found enough index write to list
                            indexFile.write(','.join(str(i) for i in oneIndexRowlist))
                            indexFile.write("\n")
                            oneIndexRowlist.clear()
                        numberOfFoundLocation += 1
                indexFile.close()
            locationFile.close()
        messageFile.close()

filename = "indexFile.txt"
#readNumberFromfileToList(filename)
testfindCharByIndexFromSourceCharFile()