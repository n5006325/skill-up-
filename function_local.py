# Filename : function_local.py

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local to', x)

func(x)
print('x is still', x)
