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

def findMaxValue(prev, new):
     if (new > prev):
          return new
     return prev

def findMax(draw, prevMax):
    maxRed = prevMax[0]
    maxGreen = prevMax[1]
    maxBlue = prevMax[2]
    for cubes in draw:
            cubeValues = cubes.strip().split(' ')
            print('Cube Values: ' + str(cubeValues))
            if (cubeValues[1] == 'red'):
                maxRed = findMaxValue(prevMax[0], int(cubeValues[0]))
            elif (cubeValues[1] == 'green'):
                maxGreen = findMaxValue(prevMax[1], int(cubeValues[0]))
            else:
                maxBlue = findMaxValue(prevMax[2], int(cubeValues[0]))
    newMax = [maxRed, maxGreen, maxBlue]
    return newMax

def power(maxValues):
     return maxValues[0] * maxValues[1] * maxValues[2]

f = open("input.txt", "r")

totalPowersList = []

for line in f:
    partitionedLine = line.rpartition(':')[2]
    gameNumber = (line.rpartition(':')[0])[4:]
    print('\nGame Number: ' + gameNumber)
    currentLine = partitionedLine.split(";")
    drawCount = 0
    validGame = True
    prevMax = [0,0,0]
    for drawLine in currentLine:
        draw = drawLine.split(',')
        drawCount = drawCount + 1
        print('Draw ' + str(drawCount) + ' : ' + str(draw)) 
        prevMax = findMax(draw, prevMax)
        print(prevMax)
        
    gamePower = power(prevMax)
    totalPowersList.append(gamePower)

totalPowers = sum(totalPowersList)
print(totalPowers)

f.close()
