class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name, "| Roll:", self.roll)


# List to store students
students = []

# Function to add student
def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    s = Student(name, roll)
    students.append(s)
    print("Student added successfully!")

# Function to display students
def display_students():
    if not students:
        print("No students found.")
    else:
        for s in students:
            s.display()

# Function to search student
def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    for s in students:
        if s.roll == roll:
            s.display()
            found = True
            break
    if not found:
        print("Student not found.")

# Menu-driven program
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")