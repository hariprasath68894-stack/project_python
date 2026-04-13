class person :
    def person(self):
        print("name:","aravindhan")
class employee(person):
    def employee(self):
        print("salary:",80000)
class manager(employee):
    def manager(self):
        print("department:","mech")
c=manager()
c.person()
c.employee()
c.manager()