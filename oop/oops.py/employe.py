class Employee:
    company = "infosys"

    def __init__(self, name):
        self.name = name

e1 = Employee("kumar")
e2 = Employee("anu")

print(e1.name, e1.company)
print(e2.name, e2.company)