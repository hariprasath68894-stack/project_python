class calculator:
    def multiply(self, a, b, c=0):
        return a * b * c
    
calc = calculator()
print(calc.multiply(10, 20))
print(calc.multiply(10, 20 ,30))