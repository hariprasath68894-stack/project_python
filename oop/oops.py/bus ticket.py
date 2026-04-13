class Bus:
    def __init__(self, price):
        self.price = price

    def total(self, persons):
        print("total:", self.price * persons)

b1 = Bus(50)
b1.total(6)