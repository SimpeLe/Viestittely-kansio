import ascii
import string
import random
import linecache



def createOneSourceCharacterList():
    """
    Creates list of all alphabetic ascii
    characters in arbitrary order 
    """
   
    # Create list of all characters
    #characters = string.printable
    characters = string.ascii_letters + string.digits + string.punctuation
    # add scandinavian characters
    characters +="äöåÄÖÅ"
    # add space characters while reading message text if space
    characters += "è"
    # add mark for newline while reading sorce text if line is ending
    characters += "á"
    # add mark for ending original message
    characters += "ô"
    print(characters)
    print(len(characters))
    # Randomize order of string
    rand_string = ''.join(random.sample(characters, len(characters)))
    #print(rand_string)
    print(random.randrange(1,800))
    print(random.randrange(1,100))
    return rand_string

def createSourceCharacterFile(size):
    """
    Creates 1Mb size file which inludes
    all alphabetic ascii characters in 
    arbitrary order 
    """
    # size in megabytes
    size = size* 1_024_000
    # length of one line which added to file 
    lengthOfOneLine = 0
    # numuber of rows in file
    numberOfRows = 0
    # number of character in file
    numberOfCharinFile = 0
    oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
    
    print(len(oneline))
    # change  own path in your computer to next line
    with open("Viestittely-kansio/sourceCharacterFile.txt", 'w') as charFile:
        while numberOfCharinFile < size:
            oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
            lengthOfOneLine = len(oneline)
            numberOfCharinFile += lengthOfOneLine
            print(lengthOfOneLine)
            print(numberOfCharinFile)
            charFile.write(oneline)
            oneline = ""

    with open(r"Viestittely-kansio/sourceCharacterFile.txt", 'r') as fp:        
        x = len(fp.readlines())
        print('Total lines  in char file:', x) # 8

    charFile.close()  


def createLocationKey(lengthOfKey):
    createdNumers = 0
    oneLinenumbers = 0
    locationLine = ""
    with open("Viestittely-kansio/locationKeyFile.txt", 'w') as locationKeyFile:
        while createdNumers < lengthOfKey:
            while oneLinenumbers < 100: # length of one line in location file
                #if oneLinenumbers < 100:
                locationLine += str(random.randrange(100)) + ","
                oneLinenumbers += 1
                print(locationLine)
                print(oneLinenumbers)
                #elif oneLinenumbers == 100: # write lines to file and set counters to zero
                 #   print(locationLine)
            print("one line is ready")
            oneLinenumbers = 0
            locationLine += "\n"
            locationKeyFile.write(locationLine)
            locationLine = ""
        
            createdNumers += 100

    with open(r"Viestittely-kansio/locationKeyFile.txt", 'r') as fp:        
        x = len(fp.readlines())
        print('Total lines  in location file:', x) # 8

    # for x in enumerate(fp.readlines()):
    #     print(x)
            
    
def searchPositionFromCharFile(originalMessageTextLine):
     originLength = len(originalMessageTextLine)
     indexInLine = 0
     sourceCharacterlineHandler  = ""
     indexInCharSourceLine = 0 # 0-300
     indexOfRowInCharFile = 0 # start from 0, maximuM around 3 000 
     startSearchingIndex = 0 # 0, 100 or 200
     oneAsciiGroupLength = 100
     numberOfCharToBeHandle = 3 # search 3 character from each sourcecharacterRow
     numberOfHandledChar = 0 # tell how many char has been handled could  be 1-3
     messagelineHandler = "" # contains one line of original message
     messageRowLength = 0 # length of message line
     lineHandled = False
     messageLentghCounter = 0
     with open("Viestittely-kansio/sourceCharacterFile.txt", 'r') as charFile:
         #charline = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
         lineread = charFile.readlines()[0]
         print("lineread") 
         print(lineread)
         #print(charline)
         charFile.seek(0)
         lineread = charFile.readlines()[1]
         print(lineread)
         #print(len(lineread))
         print("debug")
         with open("Viestittely-kansio/positionFile.txt", 'w') as positionFile:
            with open("Viestittely-kansio/origMessageFile.txt", 'r') as messageFile:
                charline = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
                # meassageline1 = linecache.getline(r"Viestittely-kansio/origMessageFile.txt", 1)
                meassageline2 = linecache.getline(r"Viestittely-kansio/origMessageFile.txt", 2)
                newline_break = ""
                rowCount = len(messageFile.readlines())
                print('Total lines  in message file:', rowCount)

                # read through hole original message file and and find relative positions from sourceCharacterfile
                for readline in range (1,rowCount+1):
                    # read one line of message and handle it
                 
                    messagelineHandler = "No"
                    messageRowLength = len(messagelineHandler) # length of original message row
                    print(messageRowLength)
                    if messageRowLength == 1:
                        print("empty line")
                        if messagelineHandler == "\n":
                            print(" this is new line")

                    
                    # handle each character in one line
                    for charInMsgLine in messagelineHandler:
                        if lineHandled == False: 
                            charFile.seek(0)
                            sourceCharacterlineHandler = charFile.readline()[indexOfRowInCharFile]
                        print("handled char in loop")
                        print(numberOfHandledChar)
                        if numberOfHandledChar == numberOfCharToBeHandle: # search 3 position of char each row from sourceCharFile
                            lineHandled = False  # set counter to right values after hangling one row
                            numberOfHandledChar = 0
                            indexOfRowInCharFile +=1 # index for reading next line of sourCharfile 
                            startSearchingIndex = 0 # index of row where start to find first char
                        if lineHandled == False: 
                            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                            sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                        lineHandled = True
                        print(sourceCharacterlineHandler)
                        print("char to be found")
                        print(charInMsgLine+"\n")

                        print("startSearchingIndex")
                        print(startSearchingIndex)
                        print("\n")

                        #indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine, startSearchingIndex)
                        indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine)
                        
                        print("index found"+"\n")
                        print(indexInCharSourceLine)
                        
                        numberOfHandledChar +=1
                        if numberOfHandledChar == 1: # set startseachindex for second char in row of sourcecharFile
                            startSearchingIndex = 100
                        elif numberOfHandledChar == 2: # set startseachindex for third char in row of sourcecharFile
                            startSearchingIndex = 200


                # messageFile.close()
                # messageFile =  open("Viestittely-kansio/origMessageFile.txt", 'r')
                # for readline in messageFile:
                #     meassageline1 = linecache.getline(r"Viestittely-kansio/origMessageFile.txt", 1)
                #     print(meassageline1)
                #     line_strip = messageFile.readline() #.strip()
                #     print(line_strip)
                #     newline_break += line_strip
                #     print(newline_break)
                
                #temp = messageFile.read().splitlines()
                #print(temp)
                rowLength = len(meassageline2)
                print(rowLength)
                currentChar = ""
                #for index in rowLength: # hjandle sinle line of original message
                currentChar = meassageline2[0]
                #indexInCharSourceLine = lineread.index(currentChar)
                print(currentChar+"\n")
                print(indexInCharSourceLine)
                print("\n")

     #charFile.close()
             
def findPositionFromSourceCharacterFile(mark):
    charline = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
    numline = linecache.getline(r"Viestittely-kansio/positionFile.txt", 1)
    #with open("Viestittely-kansio/positionFile.txt", 'w') as positionFile:
    print(charline)
    print(numline)
    index = 1
    return index


def setFinalPositionInCryptedMessage():
    pass


def testsearchPositionFromCharFile():
    indexInLine = 0
    indexInCryptedMessage = 0
    indexCounter = 0
    sourceCharacterlineHandler  = ""
    indexInCharSourceLine = 0
    indexOfRowInCharFile = 0
    startSearchingIndex = 0
    oneAsciiGroupLength = 100
    numberOfCharHandle = 3 # search 3 cracter from each sorcecharacterRow
    numberOfHandledChar = 0
    messagelineHandler = "" # contains one line of original message
    messageRowLength = 0 # length of message line
    lineHandled = False
    messageLentghCounter = 0
    indexrowrofile = ""
    messagelineHandler = "No one" + "\n" + "shall"
    with open("Viestittely-kansio/sourceCharacterFile.txt", 'r') as charFile:

        for charInMsgLine in messagelineHandler:
            #sourceCharacterlineHandler = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
            # if lineHandled == False:  # this refers to reading and handling one sourceCharacterfile
            #     charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
            #     sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
            #     print("index of row in char file " + str(indexOfRowInCharFile)+ "\n")
            #     #print(indexOfRowInCharFile)
            #     lineHandled = True
                #sourceCharacterlineHandler = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
                # sourceCharacterlineHandler = charFile.readline()[0]
            print("handled char in loop " + str(numberOfHandledChar) +"\n")
            #print(numberOfHandledChar)
            if numberOfHandledChar == numberOfCharHandle: # 3
                print("set counters to zero\n")
                lineHandled = False
                numberOfHandledChar = 0
                indexOfRowInCharFile +=1
                startSearchingIndex = 0
            if lineHandled == False:  # this refers to reading and handling one sourceCharacterfile
                charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                sourceCharacterlineHandler = charFile.readlines()[indexOfRowInCharFile]
                print("index of row in char file " + str(indexOfRowInCharFile)+ "\n")
                #print(indexOfRowInCharFile)
                lineHandled = True
                #sourceCharacterlineHandler = linecache.getline(r"Viestittely-kansio/sourceCharacterFile.txt", 1)
                # sourceCharacterlineHandler = charFile.readline()[0]
            print("handled char in loop " + str(numberOfHandledChar) +"\n")
               # indexInCryptedMessage = 0
            # if lineHandled == False: 
            #     k = 2
            #     sourceCharacterlineHandler = charFile.readlines()[0]
            #lineHandled = True
            #print(sourceCharacterlineHandler)
            print("char to be found " + str(charInMsgLine)+ "\n")
            #print(charInMsgLine+"\n")

            print("startSearchingIndex " + str(startSearchingIndex)+ "\n")
            #print(startSearchingIndex)
            #print("\n")
            if charInMsgLine == " ":
                charInMsgLine = "è"
            elif charInMsgLine == "\n":
                charInMsgLine = "á"
            elif charInMsgLine == "EOF":
                charInMsgLine = "ô"

            indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine, startSearchingIndex)
            
            print("index found "+ str(indexInCharSourceLine) +"\n")
            #print(indexInCharSourceLine)

            
            if numberOfHandledChar == 0:
                indexInCryptedMessage = indexInCharSourceLine
                indexrowrofile += str(indexInCryptedMessage)+","
                startSearchingIndex = 100
            elif numberOfHandledChar == 1: # set startseachindex for second char in row of sourcecharFile
                startSearchingIndex = 200
                indexCounter = (100 - indexInCryptedMessage) + (indexInCharSourceLine - 100)
                indexInCryptedMessage = indexCounter
                indexrowrofile += str(indexInCryptedMessage)+","
            elif numberOfHandledChar == 2: # set startseachindex for third char in row of sourcecharFile
                #startSearchingIndex = 200
                indexCounter = (200 - indexInCryptedMessage) + (indexInCharSourceLine - 200)
                indexInCryptedMessage = indexCounter
                indexrowrofile += str(indexInCryptedMessage)+","
            numberOfHandledChar +=1    
        print(indexrowrofile)


#createOneSourceCharacterList()
#createSourceCharacterFile(1)
#createLocationKey(8000)
#searchPositionFromCharFile("hgsah")
#findPositionFromSourceCharacterFile("s")
testsearchPositionFromCharFile()

#oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
#print(len(oneline))
#print("one line") 


