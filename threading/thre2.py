import threading
def numbers():
    for i in range(1,6):
        print("number:",i)

def letter():
    for ch in['a','b','c','d','e']:
        print("letter:",ch)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letter)
t1.start()
t2.start()
t1.join()
t2.join()
print("thread finished")