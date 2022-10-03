class Node:
    def __init__(self, data, left=None, right=None):
        # set data in the allocated node and return it
        self.data = data
        self.next = None
 
 
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0
 
    # Utility function to dequeue the front element
    def dequeue(self):          # delete at the beginning
        if self.front is None:
            print('Queue Underflow')
            exit(-1)
 
        temp = self.front
        print('Removing…', temp.data)
 
        # advance front to the next node
        self.front = self.front.next
 
        # if the list becomes empty
        if self.front is None:
            self.rear = None
 
        # decrease the node's count by 1
        self.count -= 1
 
        # return the removed item
        return temp.data
 
    # Utility function to add an item to the queue
    def enqueue(self, item):    # insertion at the end
        # allocate the node in a heap
        node = Node(item)
        print('Inserting…', item)
 
        # special case: queue was empty
        if self.front is None:
            # initialize both front and rear
            self.front = node
            self.rear = node
        else:
            # update rear
            self.rear.next = node
            self.rear = node
 
        # increase the node's count by 1
        self.count += 1
 
    # Utility function to return the top element in a queue
    def peek(self):
        # check for an empty queue
        if self.front:
            return self.front.data
        else:
            exit(-1)
 
    # Utility function to check if the queue is empty or not
    def isEmpty(self):
        return self.rear is None and self.front is None
 
    # Function to return the size of the queue
    def size(self):
        return self.count
 
 
if __name__ == '__main__':
 
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
 
    print('The front element is', q.peek())
 
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
 
    if q.isEmpty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
