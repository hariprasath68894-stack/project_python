class Node:
 def __init__(self, data):

   self.data = data
   self.left = None
   self.right = None

root = Node ("A")
root. left = Node("B")
root.right = Node("C")

if root.left. left is None and root.left.right is None:
 print(root.left.data, "is a Leaf Node")
if root.right.left is None and root.right.right is None:
 print(root.right.data, "is a Leaf Node")