f = open("input.txt", "r")
# Run through each line
totalValue = 0
numberStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in f:
  print(line)
  numbers = []

  for string in numberStrings:
    if string in line:
      print(string, line.index(string))

  for character in line:    
    if (character.isnumeric()):
      numbers.append(character)

  value = numbers[0] + numbers[len(numbers) - 1]
  #print(value)
  totalValue = totalValue + int(value)
  #print(numbers[0] + numbers[len(numbers) - 1])

print(totalValue)
f.close()