class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("none")

    def insert_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = node(data)

        if self.head is None:
           self.head = new_node
           return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print("Original List:")
ll.traverse()

ll.insert_begin(5)
print("After Insert at Begining:")
ll.traverse()

ll.insert_end(40)
print("After Insert at End:")
ll.traverse()

ll.delete_first()
print("After Delete First:")
ll.traverse()

ll.delete_last()
print("After Delete Last:")
ll.traverse()