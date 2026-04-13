try:
    filename = input("enter file name:")
    data = input("enter text:")
    if filename == "":
        raise Exception("file name cannot be empty")
    f = open(filename, "w")
    f.write(data)
    print("data written successfully")
except Exception as e:
    print("error:", e)