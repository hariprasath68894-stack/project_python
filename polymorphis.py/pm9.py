class person:
    def details(self):
        print("person details")

class Employee(person):
    def details(self):
        print("Employee details")

class Manager(Employee):
    def details(self):
        print("Manager details")

p = person()
e = Employee()
m = Manager()

p.details()
e.details()
m.details()