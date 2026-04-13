class animal:
    def greet(self):
        print("animal sounds ")

class dog(animal):
    def method(self):
        print("dog sound is bark")
    
class cat:
    def sound(self):
        print("cat sound is meow")
    
s = dog()
e = cat()
s.greet()
s.method()
