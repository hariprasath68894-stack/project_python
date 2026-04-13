def natural_numbers(n):
    print("Natural Numbers:")
    for i in range(1, n+1):
        print(i, end=" ")
    print()

def even_numbers(n):
    print("Even Numbers:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def odd_numbers(n):
    print("Odd Numbers:")
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def fibonacci(n):
    print("Fibonacci Series:")
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Main program
print("1. Natural Numbers")
print("2. Even Numbers")
print("3. Odd Numbers")
print("4. Fibonacci Series")

choice = int(input("Enter your choice: "))
limit = int(input("Enter the limit: "))

if choice == 1:
    natural_numbers(limit)
elif choice == 2:
    even_numbers(limit)
elif choice == 3:
    odd_numbers(limit)
elif choice == 4:
    fibonacci(limit)
else:
    print("Invalid choice")