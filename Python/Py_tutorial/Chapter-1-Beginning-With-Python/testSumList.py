def sumList(nums):
    '''Return the sum of the numbers in nums.'''
    sum = 0
    for num in nums:
        # nextSum = sum + num
        # sum = nextSum
        
        sum = sum + num
    return sum

def main():
    print(sumList([2, 3, 6, 7]))
    print()
    print(sumList([0, 9, 6, 2]))
    print()
    print(sumList([]))
    
main()