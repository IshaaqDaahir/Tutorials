num = float(input('Enter a number here:\n'))

total = 0
nums = []
while num != 0:
    nums.append(num)
    total = total + num
    num = float(input('Enter number here:\n'))

print(f'The sum of the numbers = {total}')
# print(f'The sum of the numbers = {sum(nums)}')
# print(f'The sum {nums} = {total}')