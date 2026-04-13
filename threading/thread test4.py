import threading

def check_even(n):
    if n % 2 == 0:
        print("even number")
num = int(input("enter a number: "))

t1 = threading.Thread(target=check_even, args=(num,))
t1.start()
t1.join()