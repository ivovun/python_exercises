# 6. Write a Python program which accepts
# a sequence of comma-separated numbers
# from user and generate a list
# and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


inp_str: str =\
    input('Write a sequence of'
          '\n comma-separated numbers: ')
x = inp_str.split(',')
print(f'List: {x}')
print(f'Tuple: {tuple(x)}')









