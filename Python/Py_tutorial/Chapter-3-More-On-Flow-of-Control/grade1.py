def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D' 
    else:
        letter = 'F'
    return letter

grade = int(input('Enter your score here:\n'))
print(f'Your grade is {letterGrade(grade)}!')

