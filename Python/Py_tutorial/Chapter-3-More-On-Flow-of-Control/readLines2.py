lines = list()
print('Enter lines of text.')
print('Enter an empty line to quit.')
line = input('Next line:\n')
while line != '':
    lines.append(line)
    line = input('Next line:\n')

print('Your lines were:\n')
for line in lines:
    print(lines)

