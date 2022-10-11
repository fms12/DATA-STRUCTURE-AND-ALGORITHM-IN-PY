#class definition
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne   #storing references in variables
	p2 = headTwo
	prev = None
  
	while p1 and p2:                        #until p1 and p2 are not null
		if p1.value < p2.value:               #checking for less value of node 
			prev = p1                           #storing it to keep track of linkedlist
			p1 = p1.next                        #point to nextnode
		else:
			if prev:                            #if prev is not null
				prev.next = p2
			prev = p2                           
			p2 = p2.next
			prev.next = p1
	
	if p1 is None:                          #if p1 is null then point prev next to p2
		prev.next = p2
	
	return headOne if headOne.value < headTwo.value else headTwo 
