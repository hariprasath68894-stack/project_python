username=input("Enter username:")
password=input("Enter password:")
if username =="admin":
    if password=="4321":
        print("Login successful")
    else:
        print("incorrect password")
else:
        print("invalid username")