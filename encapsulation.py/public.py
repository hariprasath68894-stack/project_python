class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

stu = student("aravind", 95)
print(stu.name)
print(stu.marks)

stu.name = "amma"
print(stu.name)