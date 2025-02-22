def printAllPositive(numberList):
    '''Print only the positve numbers in numberList.'''

    for num in numberList:
        if num > 0:
            print(num)

printAllPositive([3, -5, 2, -1, 0, 7])