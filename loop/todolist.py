task = []
while True:
    print("\n1.add task")
    print("2.view task")
    print("3.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
       task = input("Enter taks: ")
       print("your added")
    elif choice == "2":
       print("Your Task:")
       for t in task:
          print("-", t)
    elif choice == "3":
       break
    else:
       print("Invalid choice")