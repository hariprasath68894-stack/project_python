class person:
    def greet(self):
        print("hello from person")

class student(person):
    def study(self):
        print("student is studying")

class employee(person):
    def work(self):
        print("employee is working")

class intern(student, employee):
    def intern_task(self):
        print("intern doing assigned tasks")

stu = student()
emp = employee()
intn = intern()

stu.greet()
stu.study()

emp.greet()
emp.work()

intn.greet()
intn.study()
intn.work()
intn.intern_task()