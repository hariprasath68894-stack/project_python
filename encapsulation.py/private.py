class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

account = BankAccount("aravindhan", 50000)

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.__name
acc = BankAccount("aravindhan",50000)
print(acc.get_balance())
print(acc.get_name())