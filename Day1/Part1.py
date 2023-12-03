f = open("input.txt", "r")
totalValue = 0

for line in f:
  numbers = []
  for character in line:    
    if (character.isnumeric()):
      numbers.append(character)

  value = numbers[0] + numbers[len(numbers) - 1]
  totalValue = totalValue + int(value)

print(totalValue)
f.close()