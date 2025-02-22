'''Fancier format string example, with "locals()".'''

x = 20
y = 30
sum = x + y
prod = x * y

# formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
# equations = formatStr.format(x, y, sum, prod)
formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
equations = formatStr.format(**locals())
print(equations)











































