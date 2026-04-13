age = int(input("enter age:"))
if age < 15:
    raise Exception("not eligible for voting")
print("eligible")