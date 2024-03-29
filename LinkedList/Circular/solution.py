# Python code to perform circular linked list operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last is not None:
            return self.last

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # assign last to newNode
        self.last = newNode

        # create link to iteself
        self.last.next = self.last
        return self.last

    # add node to the front
    def addFront(self, data):

        # check if the list is empty
        if self.last is None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the current first node in the newNode
        newNode.next = self.last.next

        # make newNode as last
        self.last.next = newNode

        return self.last

    # add node to the end
    def addEnd(self, data):
        # check if the node is empty
        if self.last is None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the last node to next of newNode
        newNode.next = self.last.next

        # point the current last node to the newNode
        self.last.next = newNode

        # make newNode as the last node
        self.last = newNode

        return self.last

    # insert node after a specific node
    def addAfter(self, data, item):

        # check if the list is empty
        if self.last is None:
            return None

        newNode = Node(data)
        p = self.last.next
        while p:

            # if the item is found, place newNode after it
            if p.data == item:

                # make the next of the current node as the next of newNode
                newNode.next = p.next

                # put newNode to the next of p
                p.next = newNode

                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def traverse(self):
        if self.last is None:
            print("The list is empty")
            return

        newNode = self.last.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.last.next:
                break
