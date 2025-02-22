def main():
    number = float(input("Enter a number: "))

    if number > 0:
        num = "Positive"
    elif number < 0:
        num = "Negative"
    else:
        num = "Zero"
    return num

print(f'This is a {main()} number!')
