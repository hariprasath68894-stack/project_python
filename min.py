a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
min1= a if a < b else b
minimum =min if min1<c else c
print("minimum number is:", minimum)