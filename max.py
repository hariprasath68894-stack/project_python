a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max1= a if a > b else b
maximum =max1 if max1>c else c
print("maximum number is:", maximum)