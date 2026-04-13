def decorator(func):
    def wrapper():
        print("brfore execution")
        func()
        print("after execution")
    return wrapper

def greet():
    print("eren!")
# manual decoration
greet = decorator(greet)

greet()