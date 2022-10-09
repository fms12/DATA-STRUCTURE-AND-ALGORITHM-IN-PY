class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None
		
	def reverse(self, head, k):
		if head == None:
		    return None
		current = head
		next = None
		prev = None
		count = 0

		while(current is not None and count < k):
			next = current.next
			current.next = prev
			prev = current
			current = next
			count += 1
		if next is not None:
			head.next = self.reverse(next, k)
		return prev

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data,end=' ')
			temp = temp.next

linlist=linkedlist()
linlist.push(3)
linlist.push(2)
linlist.push(1)
linlist.push(6)
linlist.push(5)
linlist.push(4)
linlist.push(9)
linlist.push(8)
linlist.push(7)

print("Given linked list: ")
linlist.printList()
linlist.head = linlist.reverse(linlist.head, 3)

print ("\nReversed Linked list: ")
linlist.printList()
