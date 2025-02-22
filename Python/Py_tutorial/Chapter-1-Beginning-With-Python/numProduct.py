def product(nums):
    prod = 1
    for n in nums:
        prod = prod * n
    return prod

def main():
    print(product([5, 4, 6]))
    
main()