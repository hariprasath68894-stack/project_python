secret_number = 8
guess = 3
while  guess != secret_number:
    guess = int(input("Enter your guess:"))
    if guess == secret_number:
        print("correct! you gussed the number.")
    else:
        print("wrong guess. try again!")