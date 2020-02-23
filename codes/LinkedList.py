# Create a LinkedList, and traverse through it.

class Node:
  def __init__(self,data):
    self.data = data
    self.node = Node
    self.next = None

class Linkedlist:
  def __init__(self):
    self.head = None

  def iterate(self):
    currentNode = self.head
    while currentNode is not None:
      print(str(currentNode.data)+ " --> ", end="")  
      currentNode = currentNode.next
    print("None")  

l = Linkedlist() 
n1 = Node(6)
n2 = Node(5)
n3 = Node(4)  
n4 = Node(3)

l.head = n1

n1.next = n2
n2.next = n3
n3.next = n4

l.iterate()

# print(l.head.next.data)

# print(n1.node)
# print(n2.next)
# print(n3.node)
# print(n4.next)
