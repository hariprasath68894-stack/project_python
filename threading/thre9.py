import threading
def task1():
    print(5*5)

t1 = threading.Thread(target=task1)
t1.start()
print("this is the main program")