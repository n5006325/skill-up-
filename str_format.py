# format method - construct string from other information

age = 20
name = "Swaroop"

print("{0} was {1} years old when he wrote this book".format(name, age))
print("Why is {0} playing with that python?".format(name))

# string concatenation

print(name + " is " + str(age) + " years old")

# decimal (.) precision of 3 for float '0.333'
print("{0:.3f}".format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '__hello__'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop worte A Byte of Python'
print('{name} worte {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a', end=' ')
print('b', end=' ')
print('c')

# escape sequences

print('What\'s your name')

print('This is the first line\nThis is the second line')

# escape sequences include \, \n, \t

print("this is the first sentence. \
this is the seond sentence")

# Raw string
print(r"Newlines are indicated by \n")

# variables - you can store any variable, the values can vary
# identifiers - identifiers are names given to identify something
