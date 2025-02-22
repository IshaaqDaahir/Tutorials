price = float(input('Enter the original price: '))
discount = float(input('Enter the discount percentage: '))

newPrice = (1 - discount / 100) * price
formatted_newPrice = format(newPrice, '.2f')

print(formatted_newPrice)