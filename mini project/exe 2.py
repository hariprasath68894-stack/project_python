try:
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    print("result:", a/b)
except zerodivisionerror:
    print("error: cannot by zero")