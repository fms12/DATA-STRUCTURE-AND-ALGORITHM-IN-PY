#CREATION OF LINKED LIST



# node structure
class Node:
  #constructor to create a new node
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  #constructor to create an empty LinkedList
  def __init__(self):
    self.head = None
 
# test the code   
# create an empty LinkedList                 
MyList = LinkedList()

#Add first node.
first = Node(10)
#linking with head node
MyList.head = first

#Add second node.
second = Node(20)
#linking with first node
first.next = second

#Add third node.
third = Node(30)
#linking with second node
second.next = third

