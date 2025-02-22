age = float(input('Enter your age please:\n'))
citizenship = float(input('Enter the length of your citizenship please:\n'))

if age >= 30 and citizenship >= 9:
    print('You are eligible to be a US Senator and Representative!')
elif age >= 25 and citizenship >= 7:
    print('You are only eligible to be a US Representative!')
elif age < 25 and citizenship < 7:
    print('You are not eligible to be neither a US Senator nor Representative!')
else:
    print('You are not eligible for the offices!')

