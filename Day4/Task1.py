f = open("test.txt", "r")

for line in f:
    print(line)
    strippedLine = line.split(':')[1]
    winningNums = strippedLine.split('|')[0].strip().split(' ')
    cardNums = strippedLine.split('|')[1].strip().split(' ')
    winningIndices = []
    for winningNum in winningNums:
        #indices = [i for i, x in enumerate(cardNums) if x == winningNum]
        for i in cardNums:
            if winningNum == i:
                winningIndices.append(i)
                print('Matching Number: ' + str(winningNum))
        #if len(winningIndices) > 0:
            #print('Matching Total: ' + str(len(winningIndices)))

    #print('Winning Numbers: ' + str(winningNums))
    print('\n\n')

f.close()