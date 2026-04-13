class Item:
    def __init__(self,price):
        self.price = price

    def __mul__(self,other):
        return self.price * other.price
i1 = Item(80)
i2 = Item(90)

print("total mark:", i1 * i2)