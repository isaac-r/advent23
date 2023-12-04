# Total Number of each colour

# Read each line and determine if combination was possible

# If combination was possible, add game id to list

# Sum list

maxRed = 12
maxGreen = 13
maxBlue = 14

def isValidDraw(colour, drawNumber):
    if (colour == 'red' and drawNumber > maxRed):
        return False
    elif (colour =='blue' and drawNumber > maxBlue):
        return False
    elif (colour == 'green' and drawNumber > maxGreen):
        return False
    else:
        return True

def isValidDrawLine(draw):
    isValid = True
    for cubes in draw:
            cubeValues = cubes.strip().split(' ')
            #print('Cube Values: ' + str(cubeValues))
            if (not isValidDraw(cubeValues[1], int(cubeValues[0]))):
                isValid = False
    return isValid
                #print('Adding game number: ' + gameNumber)
            #print(int(cubeValues[0]))
            #print(cubeValues[1])

f = open("input.txt", "r")

validGames = []

for line in f:
    partitionedLine = line.rpartition(':')[2]
    gameNumber = (line.rpartition(':')[0])[4:]
    print('\nGame Number: ' + gameNumber)
    currentLine = partitionedLine.split(";")
    drawCount = 0
    validGame = True
    for drawLine in currentLine:
        draw = drawLine.split(',')
        drawCount = drawCount + 1
        print('Draw ' + str(drawCount) + ' : ' + str(draw))
        if(not isValidDrawLine(draw)):
            validGame = False
    if (validGame):
        validGames.append(int(gameNumber))

validGamesScore = sum(validGames)
print(validGamesScore)

    #print(currentLine)

f.close()
