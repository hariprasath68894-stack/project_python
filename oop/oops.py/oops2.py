class student:
    def __init__(self, brand, colour,price):
        self.brand = brand
        self.colour = colour
        self.price = price

# creating object 
s1 = student("usha", "red" , 1000)

print(s1.brand)
print(s1.price)
print(s1.colour)