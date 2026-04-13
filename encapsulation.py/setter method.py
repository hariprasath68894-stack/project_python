class student:
    def _init_(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid marks")
stu = student("kalaiselvan", 99)
stu.set_marks(109)
stu.set_marks(89)
print(stu.get_marks())