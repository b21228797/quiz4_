"""
 Example:
 Using readline() to read a file line by line in Python
"""

ListOfLines = ["0 The Road goes ever on and on", "1 Down from the door where it began",
               "2 Now far ahead the Road has gone", "3 And I must follow, if I can", "4 Pursuing it with eager feet"
    , "5 Until it joins some larger way", "6  Where many paths and errands meet", "7 And whither then? I cannot say",
               "0 There was plenty of everything left for Frodo",
               "1 as well as the books, pictures were left in his possession",
               "2 There was, however, no sign nor mention of money or jewellery",
               "3 not a penny-piece or a glass bead was given away",
               "0 There were many Bagginses and Boffins", "1 there were various Grubbs, and various Chubbs",
               "2 and a selection of Burrowses, Brockhouses and Proudfoots",
               "3 Some of these were only connected with Bilbo, and some",
               "4 of them had hardly ever been in Hobbiton before",
               "5 The Sackville-Bagginses were not forgotten", "6 They disliked Bilbo and detested Frodo",
               "7 written in golden ink"

               ]


# Function to create our test file
def createFile():
    wr = open("inputFile.txt", "w")
    for line in ListOfLines:
        # write all lines
        wr.write(line)
        wr.write("\n")
    wr.close()


# Function to demo the readlines() function
def readFile():
    rd = open("inputFile.txt", "r")

    # Read list of lines
    out = []  # list to save lines
    while True:
        # Read next line
        line = rd.readline()
        # If line is blank, then you struck the EOF
        if not line:
            break;
        out.append(line.strip())

    # Close file
    rd.close()

    return out


# Main test
def main():
    # create inputfile.txt
    createFile()

    # read lines from inputfile.txt
    outList = readFile()

    # Iterate over the lines
    for line in outList:
        print(line.strip())

        # Run Test


if __name__ == "__main__":
    main()