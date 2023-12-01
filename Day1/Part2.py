from operator import itemgetter
f = open("input.txt", "r")
# Run through each line
totalValue = 0
numberStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in f:
  print(line)
  numbers = []

  for string in numberStrings:
    if string in line:
      #print(numberStrings.index(string) + 1, line.index(string))
      stringNumberList = [numberStrings.index(string) + 1, line.index(string)]
      #print(stringNumberList)
      #newNumbers.insert(numberStrings.index(string) + 1, line.index(string))
      numbers.append(stringNumberList)

  for character in line:    
    if (character.isnumeric()):
      #print(character, line.index(character))
      characterNumberList = [int(character), line.index(character)]
      #print(characterNumberList)
      numbers.append(characterNumberList)
  print(numbers)

  sortedList = sorted(numbers, key=itemgetter(1))

  requiredVals = [sortedList[0][0], sortedList[len(sortedList) - 1][0]]

  print(requiredVals)

  print(sortedList)
  #value = numbers[0] + numbers[len(numbers) - 1]
  #print(value)
  #totalValue = totalValue + int(value)
  #print(numbers[0] + numbers[len(numbers) - 1])

print(totalValue)
f.close()