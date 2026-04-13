class Employee:
    def _init_(self, name, salary):
        self._name = name
        self._salary = salary
emp = Employee("aravindhan", 50000)
print(emp._salary)

class Manager(Employee):
    def show_salary(self):
        print(f"salary: {self._salary}")

mgr = Manager("aravindhan",80000)
mgr.show_salary()