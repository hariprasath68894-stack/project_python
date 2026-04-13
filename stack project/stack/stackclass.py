class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if len(self.stack) ==0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top:", self.stack[-1])

    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.size
    
    def display(self):
        print("Stack:", self.stack)


s =Stack(3)

s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()

s.pop()
s.peek()

print("Empty?", s.isEmpty())
print("Full?", s.isFull())