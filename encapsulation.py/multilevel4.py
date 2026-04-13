class person:
    def greet(self):
        print("hello from person")

class student(person):
    def study(self):
        print("student is studying")
    
class Empoloyee:
    def work(self):
        print("employee is working")
    
s = student()
e = Empoloyee()
s.greet()
s.study()