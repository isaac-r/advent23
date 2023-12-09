import numpy as np

### FUNCTIONS ###
def build2dArray(inputFile):

    inputList = []

    for line in inputFile:
        lineList = []

        for ch in line.strip():
            lineList.append(str(ch))

        inputList.append(np.array(lineList))

    arr = np.array(inputList)

    return arr

def isSymbol(ch):
    if ch == '*':
        return True
    return False

def constructNumber(arr, pos_x, pos_y):
    num = str(arr[pos_x][pos_y])
    print('Test: (' +  str(pos_x) + ',' + str(pos_y) + ')')
    print('Number: ' + str(arr[pos_x][pos_y]))
    arr[pos_x][pos_y] = '.'
    if pos_y-1 >= 0 and arr[pos_x][pos_y-1].isnumeric() and arr[pos_x][pos_y-1] != '.':
        num = str(arr[pos_x][pos_y-1]) + num
        arr[pos_x][pos_y-1] = '.'

        if pos_y-2 >= 0 and arr[pos_x][pos_y-2].isnumeric() and arr[pos_x][pos_y-2] != '.':
            num = str(arr[pos_x][pos_y-2]) + num
            arr[pos_x][pos_y-2] = '.'

    if pos_y+1 < len(arr[0]) and arr[pos_x][pos_y+1].isnumeric() and arr[pos_x][pos_y+1] != '.':
        num = num + str(arr[pos_x][pos_y+1])
        arr[pos_x][pos_y+1] = '.'

        if pos_y+2 < len(arr[0]) and arr[pos_x][pos_y+2].isnumeric() and arr[pos_x][pos_y+2] != '.':
            num = num + str(arr[pos_x][pos_y+2])
            arr[pos_x][pos_y+2] = '.'

    return int(num), arr

def adjacentNumbers(arr, x, y):
    # clockwise check
    numbersList = []
    if y-1 >= 0 and x-1 >= 0:
        if arr[x-1][y-1].isnumeric() and arr[x-1][y-1] != '.':
            (num, array) = constructNumber(arr, x-1, y-1)
            arr = array
            numbersList.append(num)
    
    if y-1 >=0:
        if arr[x][y-1].isnumeric() and arr[x][y-1] != '.':
            (num, array) = constructNumber(arr, x, y-1)
            arr = array
            numbersList.append(num)

    if y-1 >=0 and x+1 < len(arr[0]):
        if arr[x+1][y-1].isnumeric() and arr[x+1][y-1] != '.':
            (num, array) = constructNumber(arr, x+1, y-1)
            arr = array
            numbersList.append(num)

    if y+1 < len(arr) and x-1 >= 0:
        if arr[x-1][y+1].isnumeric() and arr[x-1][y+1] != '.':
            (num, array) = constructNumber(arr, x-1, y+1)
            arr = array
            numbersList.append(num)
    
    if y+1 < len(arr):
        if arr[x][y+1].isnumeric() and arr[x][y+1] != '.':
            (num, array) = constructNumber(arr,x,y+1)
            arr = array
            numbersList.append(num)

    if y+1 < len(arr) and x+1 < len(arr[0]):
        if arr[x+1][y+1].isnumeric() and arr[x+1][y+1] != '.':
            (num, array) =  constructNumber(arr,x+1,y+1)
            arr = array
            numbersList.append(num)

    if x-1 >= 0:
        if arr[x-1][y].isnumeric() and arr[x-1][y] != '.':
            (num, array) = constructNumber(arr,x-1,y)
            arr = array
            numbersList.append(num)
    
    if x+1 < len(arr[0]):
        if arr[x+1][y].isnumeric() and arr[x+1][y] != '.':
            (num, array) = constructNumber(arr,x+1,y)
            arr = array
            numbersList.append(num)

    return numbersList

### START PROJECT ###
# import txt file
f = open("input.txt", "r")
# convert to 2-d array
inputArray = build2dArray(f)

cols = len(inputArray[0])
rows = len(inputArray)

total = 0

for row in range(rows):
    rowTotal = 0
    for col in range(cols):
        # is this a symbol?
        subTotal = 0
        if isSymbol(inputArray[col][row]):
            # is adjacent to number(s)
            numbersList = adjacentNumbers(inputArray,col,row)
            if len(numbersList) == 2:
                print('Coords: (' + str(col) + ',' + str(row) + ')')
                print('Symbol: ' + inputArray[col][row])
                print('Numbers: ' + str(numbersList))
                subTotal = numbersList[0] * numbersList[1]
                #print('Numbers: ' + str(subTotal))
            #subTotal = sum(numbersList)
            
        if subTotal > 0:
            total = total + subTotal
            print(str(subTotal) + '\n')
    

print(total)
f.close()