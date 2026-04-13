class person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __add__(self, other):
        return self.first + " " + other.last
    
p1 = person("hariprasath", "h")
p2 = person("sathish", "dada")
print("Full name:", p1 + p2)