try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("error: file not found")
finally:
    try:
        f.close()
        print("file closed successfully")
    except:
        print("file was not opened")
        