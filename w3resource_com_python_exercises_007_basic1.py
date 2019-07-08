# 7. Write a Python program to accept
# filename from the user and print
# the extension of that.
# Sample filename : abc.java
# Output : java


x: str = input('input file name'
               'aka abc.java: ')

arr_str = x.split('.')
print(f'extension is: {arr_str[-1]}')








