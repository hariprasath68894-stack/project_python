try:
    mark = int(input("enter mark:"))

    if mark < 0 or mark > 100:
        raise Exception("invalid mark range")
    if mark >= 90:
        print("grade: A")
    elif mark >= 75:
        print("grade: B")
    elif mark >= 50:
        print("grade: C")
    else:
        print("fail")

except ValueError:
        print("invalid input")
except Exception as e:
     print("error:", e)
    