"""
Create a Doubly Linked List class with the following methods:
    - insert_at_head
    - insert_at_tail
    - insert_at_index
    - remove_at_head
    - remove_at_tail
    - remove_at_index
    - get_at_index
    - print_list
    - print_list_reverse
    - get_length
    - peek_head
    - peek_tail
    - is_empty
    - clear
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next: Node = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head: Node = None
        self.tail: Node = None

    def __str__(self):
        """
        Print the look on the linked list
        """
        nodes = ""
        node = None
        for i in range(self.length):
            if node is None:
                node = self.head
            else:
                node = node.next

            if i == self.length - 1:
                nodes += str(node)
                break

            nodes += str(node) + " <-> "

        return nodes

    def insert_at_head(self, node: Node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return

        self.length += 1
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_tail(self, node: Node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return

        self.length += 1
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert_at_index(self, node: Node, index: int):
        if index < 0 or index > self.length:
            raise IndexError

        if index == self.length:
            self.insert_at_tail(node)
            return

        if index == 0:
            self.insert_at_head(node)
            return

        self.length += 1
        rnode = self.__get_at_index(index)

        rnode.prev.next = node
        node.prev = rnode.prev
        rnode.prev = node
        node.next = rnode

    def remove_at_head(self):
        if self.length == 0:
            return

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
            return

        rnode = self.head.next
        rnode.prev = None
        self.head.next = None
        self.head = rnode

    def remove_at_tail(self):
        if self.length == 0:
            return

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
            return

        lnode = self.tail.prev
        self.tail.prev = None
        lnode.next = None
        self.tail = lnode

    def remove_at_index(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            raise IndexError

        if index == self.length - 1:
            self.remove_at_tail()
            return

        if index == 0:
            self.remove_at_head()
            return

        self.length -= 1
        cnode = self.__get_at_index(index)
        cnode.next.prev = cnode.prev
        cnode.prev.next = cnode.next
        cnode.prev = None
        cnode.next = None

    def __get_at_index(self, index) -> Node:
        if index < 0 or index >= self.length or self.length == 0:
            return None

        node = None
        for _ in range(index + 1):
            if node is None:
                node = self.head
                continue

            node = node.next

        return node

    def get_at_index(self, index):
        node = self.__get_at_index(index)
        if node is not None:
            return node.data
        raise IndexError

    def get_length(self):
        return self.length

    def print_list(self):
        print(str(self))

    def get_list_reverse(self):
        nodes = ""
        node = None
        for i in range(self.length, 0, -1):
            if node is None:
                node = self.tail
            else:
                node = node.prev

            if i == 1:
                nodes += str(node)
                break

            nodes += str(node) + " <-> "

        return nodes

    def print_list_reverse(self):
        print(self.get_list_reverse())
