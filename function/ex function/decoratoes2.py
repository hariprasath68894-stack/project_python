def decorator(func):
    def wrapper(name):
        print("brfore execution")
        func(name)
        print("after execution")
    return wrapper

@decorator
def greet(name):
    print(f"hello {name}")

greet("Hari")