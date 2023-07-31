import ascii
import string
import random
import linecache
import pickle
#import numpy as np



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
    Creates parameter "size" Mbyte sizes file which inludes
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
    with open("sourceCharacterFile.txt", 'w') as charFile:
        while numberOfCharinFile < size:
            oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
            lengthOfOneLine = len(oneline)
            numberOfCharinFile += lengthOfOneLine
            print(lengthOfOneLine)
            print(numberOfCharinFile)
            charFile.write(oneline)
            oneline = ""

    with open(r"sourceCharacterFile.txt", 'r') as fp:        
        x = len(fp.readlines())
        print('Total lines  in char file:', x) # 8

    charFile.close()  


def createLocationKey(lengthOfKey):
    """
    Creates location key file, original messages index found from
    sourceCharfile will be written in these location to final message
    """
    createdNumers = 0
    oneLinenumbers = 0
    locationLine = ""
    with open("locationKeyFileTest.txt", 'w') as locationKeyFile:
        while createdNumers < lengthOfKey:
            while oneLinenumbers < 100: # length of one line in location file
                #if oneLinenumbers < 100:
                locationLine += str(random.randrange(102)) + ","
                oneLinenumbers += 1
                print(locationLine)
                print(oneLinenumbers)
                #elif oneLinenumbers == 100: # write lines to file and set counters to zero
                 #   print(locationLine)
            print("one line is ready")
            oneLinenumbers = 0
            locationLine = locationLine[:-1] # remove last ","
            locationLine += "\n"
            locationKeyFile.write(locationLine)
            locationLine = ""
        
            createdNumers += 100

    with open(r"locationKeyFile.txt", 'r') as fp:        
        x = len(fp.readlines())
        print('Total lines  in location file:', x) 

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
         with open("positionFile.txt", 'w') as positionFile:
            with open("origMessageFile.txt", 'r') as messageFile:
                charline = linecache.getline(r"sourceCharacterFile.txt", 1)
                # meassageline1 = linecache.getline(r"Viestittely-kansio/origMessageFile.txt", 1)
                meassageline2 = linecache.getline(r"origMessageFile.txt", 2)
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
    charline = linecache.getline(r"sourceCharacterFile.txt", 1)
    numline = linecache.getline(r"positionFile.txt", 1)
    #with open("Viestittely-kansio/positionFile.txt", 'w') as positionFile:
    print(charline)
    print(numline)
    index = 1
    return index


def writeFinalMessageFileByNumber():
    """
    Create final message file by number. Set index by location to message rows
    """

    listOfOneRowLocation=[] # read one row of location from file to this list
    oneMessagerow=[] # create one row of messages and write to file
    listOfOneRowIndex=[] # read one row of index from file to this list
    lengthOfOneMessageRow = 100
    lengthOfOneLocationRow = 0
    lengthOfOneIndexRow = 0
    numberOfIndexRowInFile = 0
    numberOfLocationRowInFile = 0
    messageRowReady = False
    lastRowOfIndex = False
    distanceOfRowIndex = 0
    indexNumber = 0 # counter for reading values fron location list
    currenLocationNumber = 0
    currenIndexNumber = 0
    locationCounter = 0 # count location together and set to final message by location 
    hanledLocationForMessageRow = 0
    #f = open(filename,"r")
    #lines = f.readlines()
    #f.seek(0)
    #filerowlen = len(f.readlines())
    #print(filerowlen)
    #f.close()
    with open("finalMessageByNumber.txt", 'w') as messageFileByNumber:
        with open("indexFile.txt", 'r') as indexFile:
             with open("locationTest.txt", 'r') as locationFile:
                indexRowLines = indexFile.readlines()
                print("index file readed")
                numberOfIndexRowInFile = len(indexRowLines)
                print("numberOfIndexRowInFile " + str(numberOfIndexRowInFile) +"\n")
                locationRowLines = locationFile.readlines()
                numberOfLocationRowInFile = len(locationRowLines)
                print("numberOfLocationRowInFile " + str(numberOfLocationRowInFile) +"\n")
                #for line in indexFile:
                for line in range(0,numberOfIndexRowInFile): # go through entire index file row by row
                    locationCounter = 0
                    indexNumber = 0
                    locationFile.seek(0) #  set file iterator to zero before read line, otherwise it will raise "index out of range" error
                    #listOfOneRowLocation = locationFile.readlines()[line]
                    listOfOneRowLocation = [int(x) for x in locationRowLines[line].split(",")] # read one location row to list
                    print(listOfOneRowLocation)
                    print("index file loop " + str(line)+ "\n")
                    listOfOneRowIndex = [int(x) for x in indexRowLines[line].split(",")] # read one index row to list
                    print(listOfOneRowIndex)
                    lengthOfOneIndexRow = len(listOfOneRowIndex)

                    if messageRowReady == False: # start creating one message row
                        print("row creating")
                        for messageRowIndex in range(0, lengthOfOneMessageRow): # fill one row with random numbers
                            oneMessagerow.append(random.randrange(102))
                            print(str(messageRowIndex)+"\n")
                    elif messageRowReady == True:
                        print("row ready")
                        hanledLocationForMessageRow = 0

                    for oneRowIndex in listOfOneRowIndex: # go through one index row and set numbers to message row by location
                        if lengthOfOneIndexRow > 100:
                            lastRowOfIndex = True
                        print("listOfOneRowIndex " + str(listOfOneRowIndex) +"\n")
                        print("oneRowIndex " + str(oneRowIndex) +"\n")
                        print("indexNumber " + str(indexNumber) +"\n")
                        #oneMessagerow[oneRowIndex] = 36
                        #messageFile.write(str(indexNumber)+",")
                        currenLocationNumber = listOfOneRowLocation[indexNumber] # read one location from list
                        locationCounter += currenLocationNumber # count together location for message row
                        oneMessagerow[locationCounter] = oneRowIndex # set index by location to message row
                        hanledLocationForMessageRow +=1 # add counter of handled location
                        if hanledLocationForMessageRow == 4:
                            hanledLocationForMessageRow = 0
                            messageFileByNumber.write(','.join(str(i) for i in oneMessagerow))
                            messageFileByNumber.write("\n")
                            messageRowReady = True
                        currenIndexNumber = oneRowIndex
                        print(listOfOneRowLocation)
                        print(oneMessagerow)
                        print("currenLocationNumber " + str(currenLocationNumber) +"\n")
                        print("currenIndexNumber " + str(currenIndexNumber) +"\n")
                        print("locationCounter " + str(locationCounter) +"\n")
                        indexNumber += 1
                    print(oneMessagerow)
                locationFile.close()
             indexFile.close()
        messageFileByNumber.close()


def setFinalPositionInCryptedMessage(listOfOneRow):
     pass
         
def writelisttofile():
    myList = [1,2,3,4]

    with open('listfile.txt', 'w') as outfile:
        outfile.write(','.join(str(i) for i in myList))
        outfile.close()

def testSearchIndexFromCharFile():
    """
    Find index of letters(original message written by user)
    from sourceCharFile and create indexFile
    """
    listOfOneRowIndex=[] # list of index
    indexInLine = 0
    indexInCryptedMessage = 0
    indexCounter = 0
    sourceCharacterlineHandler  = "" # read one row of character to this 
    indexInCharSourceLine = 0 # number of index found from row
    startSearchingIndex = 0 # start index when finding index from row
    indexOfRowInCharFile = 0 # current row number while proceeding sourceCharFile
    numberOfRowsInCharfile = 0 # numberd of rows in char file, when reach end set indexOfRowInCharFile to zero
    oneAsciiGroupLength = 100
    numberOfCharHandle = 3 # search 3 cracter from each sorcecharacterRow
    numberOfHandledChar = 0
    messagelineHandler = "" # contains one line of original message
    messageRowLength = 0 # length of message line
    lineHandled = False
    messageLentghCounter = 0
    indexrowrofile = ""
    indexrowflineHandled = False
    
    #messagelineHandler = "No one" + "\n" + "shall"
    with open("indexFile.txt", 'w') as indexFile:
        with open("origMessageFile.txt", 'r') as messageFile:
            with open("sourceCharacterFile.txt", 'r') as charFile:
                numberOfRowsInCharfile = len(charFile.readlines())
                charFile.seek(0)
                print('Total lines  in charFile file:', numberOfRowsInCharfile) 
                for readline in messageFile: # go through hole original message(write by user) file line by line
                # messagelineHandler = linecache.getline(r"origMessageFile.txt", 1)
                # print(messagelineHandler)
                    print("print readline\n")
                    print (readline)
                    messagelineHandler =  readline #messageFile.readline()
                    #line_strip = messageFile.readline() #.strip()
                    print(messagelineHandler)
                    #newline_break += line_strip
                    #print(newline_break)
                    
                    for charInMsgLine in messagelineHandler: # go through entire row of original message char by char and found index from
                        # sourcecharfile
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
                        if lineHandled == False:  # this refers to reading and handling one source Character row
                            charFile.seek(0) # IMPORTANT! set file iterator to zero before read line, otherwise it will raise "index out of range" error
                            if numberOfRowsInCharfile == indexOfRowInCharFile: # end of file, start reading from first row
                                indexOfRowInCharFile = 0
                                print("start reading from row zero\n")

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
                        if charInMsgLine == " " or charInMsgLine == "\t":
                            charInMsgLine = "è"
                        elif charInMsgLine == "\n" or charInMsgLine == "\v" or charInMsgLine == "\r":
                            charInMsgLine = "á"
                        #elif charInMsgLine == "EOF":
                        #    charInMsgLine = "ô"

                        indexInCharSourceLine = sourceCharacterlineHandler.find(charInMsgLine, startSearchingIndex)
                        
                        print("index found "+ str(indexInCharSourceLine) +"\n")
                        #print(indexInCharSourceLine)

                        
                        if numberOfHandledChar == 0:
                            #indexInCryptedMessage = indexInCharSourceLine
                            #indexrowrofile += str(indexInCharSourceLine)+","
                            listOfOneRowIndex.append(indexInCharSourceLine)
                            startSearchingIndex = 100
                        elif numberOfHandledChar == 1: # set startseachindex for second char in row of sourcecharFile
                            startSearchingIndex = 200
                            #indexCounter = (100 - indexInCryptedMessage) + (indexInCharSourceLine - 100)
                            #indexInCryptedMessage = indexCounter
                            #indexrowrofile += str(indexInCharSourceLine)+","
                            listOfOneRowIndex.append(indexInCharSourceLine)
                        elif numberOfHandledChar == 2: # set startseachindex for third char in row of sourcecharFile
                            startSearchingIndex = 200
                            #indexCounter = (200 - indexInCryptedMessage) + (indexInCharSourceLine - 200)
                            #indexInCryptedMessage = indexCounter
                            #indexrowrofile += str(indexInCharSourceLine)+","
                            listOfOneRowIndex.append(indexInCharSourceLine)
                        numberOfHandledChar +=1
                        
                        # if(len(indexrowrofile) > 300 or len(indexrowrofile) == 300):
                        #     indexFile.write(indexrowrofile+"\n")
                        #     indexrowrofile = ""
                        #     indexrowflineHandled = True
                            
                        if(len(listOfOneRowIndex) == 100):
                           #indexrowflineHandled = True
                            indexFile.write(','.join(str(i) for i in listOfOneRowIndex)) # write row to file
                            indexFile.write("\n")
                            listOfOneRowIndex.clear()


                # end of file, set end mark(ô) for message
                indexInCharSourceLine = sourceCharacterlineHandler.find("ô", 0) # ô char means end of message, start searching from index zero of this mark 
                print("index found for ending message "+ str(indexInCharSourceLine) +"\n")
                indexrowrofile += str(indexInCharSourceLine)
                listOfOneRowIndex.append(indexInCharSourceLine)
                print(indexrowrofile)
                if indexrowflineHandled == False: # write last row of index
                    indexFile.write(','.join(str(i) for i in listOfOneRowIndex))
                    listOfOneRowIndex.clear()
                    #indexFile.write(indexrowrofile)

            charFile.close()
        messageFile.close()
    indexFile.close()

def testPickle():
 
    # List of numbers
    L = [1, 2, 3, 4, 5]
    
    # Open the file in write binary mode
    with open('list.txt', 'wb') as F:
        # Dump the list to file
        pickle.dump(L, F)
    
    # To import the list back from disk
    with open ('list.txt', 'rb') as F:
        L2 = pickle.load(F)
    
    # Print the list and see if it looks the same
    print(L2)
    
    # Close the file
    F.close()


def testList():
    F = open('lista.txt', 'w')
 
    # List of numbers
    L = [1, 2, 3, 4, 5, 6, 7]
    
    # Use a list comprehension to convert the 
    # numbers to strings then join all strings 
    # using a new line
    F.write([str(x) for x in L])
    #F.write("\n".join([str(x) for x in L]))
    
    # Close the file
    F.close()

def writeListLines():
    numbers = []
    numbers.append(str(121))
    numbers.append(str(245))
    numbers.append(str(453))
    numbers.append(str(674))
    numbers.append("\n")
    print(numbers)
    print("writelist")

    with open('numbers.txt', 'w') as fp:
        fp.writelines(numbers)

def readListLines():
    numbers = []

    # open file and read the content in a list
    with open('nums_method_1b.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            print(str(x))
            # add current item to the list
            numbers.append(str(x))

    # display list
    print(numbers)
    print(numbers)

# def generate_specific_rows(filePath, row_indices=[]):
#     with open(filePath) as f:
#         # using enumerate to track line no.
#         for i, line in enumerate(f):
#             #if line no. is in the row index list, then return that line
#             if i in row_indices:
#                 yield line

# def readRowList():
#     gen = generate_specific_rows("numbers.txt",row_indices = [1])
#     data = np.loadtxt(gen, delimiter=",")
#     print(data)


def saveListOfNumb():
    nums = [32423, 30902, 28153, 31651, 36795, 28939, 26144, 21940]
    nums2 = [944, 67, 576, 74, 23, 54, 4144, 2140]
    fp  = open('nums_method_1b.txt', 'w')
    tmp = (','.join(str(n)for n in nums))
    fp.write('{}'.format(tmp))
    tmp2 = (','.join(str(n)for n in nums2))
    fp.write('{}'.format(tmp2))
    fp.close()


def readNumList():
    list1=[]
    list2=[]
    f = open("nums_method_1b.txt","r")
    lines = f.readlines()
    x = len(f.readlines())
    print(x)
    f.close()
    list1 = [int(x) for x in lines[0].split(",")]
    list2 = [int(x) for x in lines[1].split(",")]

    print(list1)
    print(list2)
    print(list1[2])
    list1 += list2
    print(list1)

def readNumListLoop():
    list1=[]
    list2=[]
    f = open("nums_method_1b.txt","r")
    lines = f.readlines()
    f.seek(0)
    x = len(f.readlines())
    print(x)
    f.close()
    for line in range(0,x):
        list1 = [int(x) for x in lines[line].split(",")]
        print(list1) 
        #list2 = [int(x) for x in lines[1].split(",")]
        list2 = list2 + list1
        print(list2)


def readOneNumList():
    list1=[]
    list2=[]
    file = open("nums_method_1b.txt","r")
    #line = file.readline()[0]
    
    #list1 = [int(x) for x in line.split(",")]
    list1 = [int(number) for number in file.readline().split(',')]
    #list2 = [int(x) for x in lines[1].split(",")]

    print(list1)
   # print(list2)
    print(list1[4])
    file.close()

def readMultipleNumList():
    list1=[]
    list2=[]
    with open("nums_method_1b.txt") as nums:   
        for line in nums:
    #line = file.readline()[0]
    
    #list1 = [int(x) for x in line.split(",")]
            #list1.append([int(number) for number in nums.readline().split(',')])
            list1 = [int(number) for number in nums.readline().split(',')]
    #list2 = [int(x) for x in lines[1].split(",")]

    print(list1)
   # print(list2)
    #print(list1[4])
    nums.close()

def readAllNimb():
    numbers = []
    with open("nums_method_1b.txt") as nums:   
        for line in nums:
            line = line.strip() # remove newline at end and other whitespace
            if line: # avoid empty lines
                n = list(map(int, line.split(", ")))
                numbers.append(n)
       
    row1, row2 = numbers 
    print(row1)
    print(row2)

def readAgain():
    numlist = []
    f=open('nums_method_1b.txt',"r")
    for line in f:
        numlist.append(line.strip('\n'))
        print(numlist)
               
def readAgain2():
    with open('nums_method_1b.txt', 'r') as f:
        lines = f.readlines()
        numbers =[int(e.strip()) for e in lines]
        print(numbers)

def readAgain3():
        with open('nums_method_1b.txt', 'r') as input_data:
            input_list= [map(int,num.split()) for num in input_data.readlines()]
        print(input_list)

def readAgain4():
    L = []
    with open('nums_method_1b.txt') as txtfile:
        for line in txtfile:
            L.append(int(line.rstrip()))
            #''.join(e for e in line if e.isalnum())
            print(line)
            #print(e)
            #int(float(input))
    print(L)

def readAgain5():
    with open('nums_method_1b.txt') as num:
        numbers = num.read()
        n= numbers.split()
        lst = []
        for x in range(len(n)):
            nu = n[x]
            print(nu)
            new_string = nu.replace(',', ' ')
            print(new_string)
            #lst.append(int(new_string))
            #lst.append(int(mytable))
        print(lst)

def removePunc():
    #s = "string. With. Punctuation?" # Sample string 
    #out = s.translate(string.maketrans("",""), string.punctuation)
    #print(out)

    txt = "Hello Sam!"
    mytable = str.maketrans("S", "P")
    print(txt.translate(mytable))

    
    txt = "32423,30902,28153,31651,36795 , 28939 , 26144 , 2194"
    mytable = str.maketrans(",", " ")
    print(txt.translate(mytable))

def removePunc2():
    #a_string = '!hi, wh?at is the weat[h]er lik?e.'
    a_string = "32423,30902,28153,31651,36795 , 28939 , 26144 , 2194"
    new_string = a_string.translate(str.maketrans('', '', string.punctuation))

    print(new_string)

def removePunc3():
    #a_string = '!hi. wh?at is the weat[h]er lik?e.'
    a_string = "32423,30902,28153,31651,36795 , 28939 , 26144 , 2194"
    new_string = a_string.replace(',', ' ')

    print(new_string)


#createOneSourceCharacterList()
#createSourceCharacterFile(1)
#createLocationKey(8000)
#searchPositionFromCharFile("hgsah")
#findPositionFromSourceCharacterFile("s")
testSearchIndexFromCharFile()
#testPickle()
#testList()
#writeListLines()
#readListLines()
#saveListOfNumb()
#readNumList()
#readNumListLoop()
#readOneNumList()
#readMultipleNumList()
#readAllNimb()
#readAgain5()
#removePunc3()
#writelisttofile()
#writeFinalMessageFileByNumber()



#oneline = createOneSourceCharacterList() + createOneSourceCharacterList() + createOneSourceCharacterList() + "\n"
#print(len(oneline))
#print("one line") 


