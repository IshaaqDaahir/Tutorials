# def multipleAll(numList, multiplier):
#     '''Return a new list containing all of the elements of numList, each multiplied by
#     multiplier.'''
    
#     newList = list()
#     for num in numList:
#         newList.append(num*multiplier)
#     return newList

# print(multipleAll([3, 1, 7], 5))

# There is also a concise syntax called list comprehension that allows you to derive a new 
# list from a given sequence.
def multipleAll(numList, multiplier):
    '''Return a new list containing all of the elements of numList, each multiplied by
    multiplier.'''
    
    newList = [multiplier*num for num in numList]
    return newList

print(multipleAll([3, 1, 7], 5))