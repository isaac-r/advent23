from operator import itemgetter

def readNumberString(line):
  numberStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  returnNumberStringList = []
  for string in numberStrings:
    startTest = line.find(string)
    endTest = line.rfind(string)
    if (startTest > -1):
     stringNumberList = [numberStrings.index(string) + 1, startTest]
     returnNumberStringList.append(stringNumberList)
    if (endTest > -1):
     stringNumberList2 = [numberStrings.index(string) + 1, endTest]
     returnNumberStringList.append(stringNumberList2)

  return returnNumberStringList

def readNumberCharacter(line, numberString):
  index = -1
  for character in line:
    index = index + 1
    if (character.isnumeric()):
      characterNumberList = [int(character), index]
      numberString.append(characterNumberList)

f = open("input.txt", "r")
totalValue = 0

for line in f:
  print(line)

  numberString = readNumberString(line)

  readNumberCharacter(line, numberString)

  sortedList = sorted(numberString, key=itemgetter(1))

  print(sortedList)

  requiredVals = [sortedList[0][0], sortedList[len(sortedList) - 1][0]]
  addedVals = str(sortedList[0][0]) + str(sortedList[len(sortedList) - 1][0])
  print(addedVals)

  totalValue = totalValue + int(addedVals)

print(totalValue)
f.close()