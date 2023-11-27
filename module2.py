# module2.py
from module1 import greet

def use_greet_function():
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

# Call the function when the module is executed directly
if __name__ == "__main__":
    use_greet_function()
