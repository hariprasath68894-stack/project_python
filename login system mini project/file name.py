try:
    filename = input("enter file name:")
    data = input("enter text:")
    if filename == nmkj:
         raise Exception("file name cannot be empty")
    f = open(filename, "w")
    f.write(data)
    print("data written successful")
except Exception as e:
    print("error:", e)
finally:
try:
    f.close()
    print("file closed")
except:
    print("file not created")