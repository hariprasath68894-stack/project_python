try:
    correct_pin = 1234
    attempts = 3

    while attempts > 0:
        pin = int(input("enter PIN:"))

        if pin == correct_pin:
            print("access granted")
            break
        else:
            attempts -= 1
            print("wrong PIN. attempts left:", attempts)

    if attempts == 0:
        raise Exception("card blocked")
    
except ValueError:
    print("invalid PIN format")

except Exception as e:
    print("error:", e)