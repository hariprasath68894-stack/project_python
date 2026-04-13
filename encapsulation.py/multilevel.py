class grandparent:
    def great_grandparent(self):
        print("hello from grandparent")

class parent(grandparent):
    def great_parent(self):
        print("hello from parent")
    
class child(parent):
    def great_child(self):
        print("hello from child")

c = child()
c.great_grandparent()
c.great_parent()
c.great_child()