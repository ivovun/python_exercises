# Question 5
# # Level 1
# #
# # Question:
# # Define a class which has at least two methods:
# # getString: to get a string from console input
# # printString: to print the string in upper case.
# # Also please include simple test function to test
# the class methods.
# #
# # Hints:
# # Use __init__ method to construct some parameters


class MyClass:

    def __init__(self):
        self.s: str = ''

    def get_string(self):
        self.s = input('введите строку: ')

    def print_string(self):
        print(self.s.upper())


n = MyClass()
n.get_string()
n.print_string()
