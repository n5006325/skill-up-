# Filename : function_varargs.py

def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,1,2,3,jack=1123,john=2231,inge=1560))
