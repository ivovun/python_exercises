def decorator_function(original_function):
    print('==1== decorator_function')
    def wrapper_function():
        print(f'==2== wrapper executed before {original_function}')
        return original_function()
    return wrapper_function
 
@decorator_function
def display():
     print(f'==3== display function run')

display()
