** TRANSVERSAL OF A LINKED LIST **



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

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

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

#print the content of list 
MyList.PrintList()

