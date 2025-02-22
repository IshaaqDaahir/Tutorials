# lines = list()
# print('Enter 3 lines of text')
# for i in range(3):
#     line = input('Next line:\n')
#     lines.append(line)

# print('Your lines were:\n') # check now
# for line in lines:
#     print(line)         

lines = list()
testAnswer = input('Press Y if you want to enter more lines:\n')
while testAnswer == 'Y':
    line = input('Next line:\n')
    lines.append(line)
    testAnswer = input('Press Y if you want to enter more lines:\n')       

print('Your lines were:\n')
for line in lines:
    print(line)