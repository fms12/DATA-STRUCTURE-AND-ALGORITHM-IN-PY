"""
Create a Singly Linked List class with the following methods:
    - insert_at_head
    - insert_at_tail
    - insert_at_index
    - remove_at_head
    - remove_at_tail
    - remove_at_index
    - get_at_index
    - get_length
    - print_list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


class LinkedList:
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

            nodes += str(node) + " -> "

        return nodes

    def insert_at_head(self, node: Node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return

        self.length += 1
        node.next = self.head
        self.head = node

    def insert_at_tail(self, node: Node):
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return

        self.length += 1
        self.tail.next = node
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
        rnode = self.__get_at_index(index - 1)
        lnode = rnode.next
        rnode.next = node
        node.next = lnode

    def remove_at_head(self):
        if self.length == 0:
            return

        self.length -= 1
        node = self.head.next
        self.head.next = None
        self.head = node

    def remove_at_tail(self):
        if self.length == 0:
            return

        self.length -= 1
        self.tail = self.__get_at_index(self.length - 1)

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
        lnode = self.__get_at_index(index - 1)
        cnode = lnode.next
        lnode.next = cnode.next
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

    def get_length(self):
        return self.length

    def print_list(self):
        return print(str(self))
