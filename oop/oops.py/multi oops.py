class student:
    def _init_(self,name,register_number,dept,subject,phone_number,place):
        self.name = name
        self.register_number = register_number
        self.dept = dept
        self.subject = subject
        self.phone_number = phone_number
        self.place = place
    def display(self):
        print("name:",self.name)
        print("register_number:",self.register_number)
        print("dept:",self.dept)
        print("subject:",self.subject)
        print("phone_number:",self.phone_number)
        print("place:",self.place)
s1 = student(
    "aravind",
    192314010,
    "mech",
    "python",
    8122051819,
    "chennai"
)
s2 = student(
    "abijith",
    192314005,
    "mech",
    "python",
    7305975159,
    "chennai"
)
s1.display()
s2.display()




        
