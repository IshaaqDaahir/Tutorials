def sumList(nums):
    '''Return the sum of the numbers in nums.'''
    sum = 0
    for num in nums:
        # nextSum = sum + num
        # sum = nextSum
        
        sum = sum + num
    return sum

print(sumList([5, 2, 4, 7]))