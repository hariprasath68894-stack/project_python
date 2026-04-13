age = int(input("enter age:"))
if age < 18:
    raise Exception("not eligible")
print("eligible")