# Filename : var.py
i= 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

# best practice to write a single 'logicl' line per 'physical' line.

# explicit line joining using backslash allows you to break up a long 'logical' line of code

# indentation (leading white spaces) is used to determine grouping of statements
# a set of statements is called a block

i = 5
# error below! Notice a single space at the start of the line
print('Value is', i)
print('I repeat, the value is', i)
