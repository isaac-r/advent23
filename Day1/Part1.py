# Read in values from input
f = open("input.txt", "r")
# Run through each line
totalValue = 0
for line in f:
  # in each line, find the first and last numbers
  #print(line)
  numbers = []
  for character in line:    
    if (character.isnumeric()):
      numbers.append(character)
      #print(character)
  #print(numbers)
  value = numbers[0] + numbers[len(numbers) - 1]
  #print(value)
  totalValue = totalValue + int(value)
  #print(numbers[0] + numbers[len(numbers) - 1])

print(totalValue)
f.close()



# combine these into one number (so find them as strings?)
# sum all of the lines and output this sum total