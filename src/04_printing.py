"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d,' % (x), 'y is %s,' % round(y,2), 'z is "%s"' % z)

# Use the 'format' string method to print the same thing
print('x is {},'.format(x),'y is {0:.2f},'.format(y),'z is "{}"'.format(z))

# Finally, print the same thing using an f-string
print(f"x is {x},",f"y is {y:.2f},",f'z is "{z}"')
