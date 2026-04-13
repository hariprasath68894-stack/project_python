try:
    username = input("enter username:")
    password = input("enter password:")

    if username == "admin" and password == "123":
        print("login successful")

    elif username == "" or password == "":
        raise ValueError("empty input not allowed")
    else:
        print("invalid credentials")
except ValueError as e:
    print("error:", e)
finally:
    print("login process 😁 completed")