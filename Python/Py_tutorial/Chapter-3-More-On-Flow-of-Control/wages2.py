def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage. Include overtime for hours over 40.
    '''

    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
        overSixtyHours = 0
    elif totalHours > 40 and totalHours <= 60:
        overtime = totalHours - 40
        regularHours = 40
        overSixtyHours = 0
    else:
        regularHours = 40
        overSixtyHours = totalHours - 60
        overtime = totalHours - 40 - overSixtyHours
        # overtime = 20
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime + (2*hourlyWage)*overSixtyHours

def main():
    hours = float(input('Enter hours worked:\n'))
    wage = float(input('Enter dollars paid per hour:\n'))
    total = calcWeeklyWages(hours, wage)

    # print(f'Wages are ${total:.2f}.')
    print('Wages are ${total:.2f}.'.format(**locals()))

main()