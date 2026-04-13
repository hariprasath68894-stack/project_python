class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def find_middle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.data
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
n1.next=n2
n2.next=n3
n3.next=n4
print("middle:",find_middle(n1))