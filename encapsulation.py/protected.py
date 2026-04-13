class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
emp = Employee("aravindhan", 50000)
print(emp._salary)

class Manager(Employee):
    def show_salary(self):
        print(f"salary: {self._salary}")
    def show_name(self):
        print(f"name: {self._name}")

mgr = Manager("aravindhan",80000)
mgr.show_salary()
mgr.show_name()