def decorator_function(original_function):
    print('==1== decorator_function')
    def wrapper_function(x):
        print(f'==2== wrapper executed before {original_function}')
        return original_function(x)
    return wrapper_function
 
@decorator_function
def display(n):
     print(f'==3== display function run, param = {n}')

display(2)
