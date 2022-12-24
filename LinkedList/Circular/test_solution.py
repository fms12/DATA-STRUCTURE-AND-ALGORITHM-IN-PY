from .solution import CircularLinkedList
import pytest

print(pytest)


def inserting_node():
    adding_elements = CircularLinkedList()
    last1 = adding_elements.addToEmpty(6)
    last2 = adding_elements.addEnd(8)
    last3 = adding_elements.addFront(2)
    last4 = adding_elements.addAfter(10, 2)
    assert adding_elements.traverse() == print(last3,last4,last1,last2)


def deleting_node():
    delete = CircularLinkedList()
    last = delete.addToEmpty(6)
    last = delete.addEnd(8)
    last = delete.addFront(2)
    last = delete.addAfter(10, 2)
    last = delete.deleteNode(last, 8)
    assert delete.traverse() == print(2,10,6)
