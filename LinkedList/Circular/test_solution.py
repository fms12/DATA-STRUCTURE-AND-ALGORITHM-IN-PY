from .solution import CircularLinkedList, Node
import pytest


def inserting_node():
    adding_elements = CircularLinkedList()
    last = adding_elements.addToEmpty(6)
    last = adding_elements.addEnd(8)
    last = adding_elements.addFront(2)
    last = adding_elements.addAfter(10, 2)
    result = adding_elements.traverse()
    assert result == print(2,10,6,8)

def deleting_node():
    delete = CircularLinkedList()
    last = delete.addToEmpty(6)
    last = delete.addEnd(8)
    last = delete.addFront(2)
    last = delete.addAfter(10, 2)
    last = delete.deleteNode(last, 8)
    result = delete.traverse()
    assert result == print(2,10,6)
