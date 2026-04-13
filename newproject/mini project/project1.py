student = {}

def add_student(name, marks):
    student[name] = marks
    print("student added")

def display_student():
    for name, marks in student.items():
        print(name, ":", marks)

add_student("sathish", 85)
add_student("hari", 90)

display_student()