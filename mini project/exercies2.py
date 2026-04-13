try:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number"))

    print("choose operation: +, -, *, /")
    op = input("enter operator:")
    
    if op == "+":
        print("result:", num1 + num2)

    elif op == "-":
        print("result:", num1 - num2)

    elif op == "*":
        print("result:", num1 * num2)

    elif op == "/":
        print("result:", num1 / num2 )
    
    else:
        print("invalid operator")

except ZeroDivisionError:
    print("error: cannot divide zero")

except ValueError:
    print("error: invalid input")

else:
    print("calculation successful")
