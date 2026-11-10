#FUNCTIONS
def hello_func():
    print("hello function")

hello_func()
hello_func()

def hi_func():
    return 'hi function'

print(hi_func())

print()

#passing arguments
def greets(greetings):
    print(f"{greetings} user")

greets("what's up!")
print()
#default arguments

def test_func(greet,name="User"):
    print(f"{greet} , {name}")
test_func('hi','sneha')
test_func('hello')