from .solution import DoublyLinkedList, Node
import pytest


def test_node():
    node = Node(1)
    assert node.data == 1


def test_node_next():
    node = Node(1)
    assert node.next is None


def test_node_prev():
    node = Node(1)
    assert node.prev is None


def test_node_repr():
    node = Node(1)
    assert repr(node) == "1"


def test_node_str():
    node = Node(1)
    assert str(node) == "1"


def test_doubly_linked_list_str():
    dll = DoublyLinkedList()
    assert str(dll) == ""

    dll.insert_at_head(Node(1))
    assert str(dll) == "1"

    dll.insert_at_head(Node(2))
    assert str(dll) == "2 <-> 1"

    dll.insert_at_head(Node(3))
    assert str(dll) == "3 <-> 2 <-> 1"


def test_doubly_linked_list_insert_at_head():
    dll = DoublyLinkedList()
    dll.insert_at_head(Node(1))
    assert dll.length == 1
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.insert_at_head(Node(2))
    assert dll.length == 2
    assert dll.head.data == 2
    assert dll.tail.data == 1


def test_doubly_linked_list_insert_at_tail():
    dll = DoublyLinkedList()
    dll.insert_at_tail(Node(1))
    assert dll.length == 1
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.insert_at_tail(Node(2))
    assert dll.length == 2
    assert dll.head.data == 1
    assert dll.tail.data == 2

    dll.insert_at_tail(Node(3))
    assert dll.length == 3
    assert dll.head.data == 1
    assert dll.tail.data == 3


def test_doubly_linked_list_insert_at_head_and_tail():
    dll = DoublyLinkedList()
    dll.insert_at_head(Node(1))
    dll.insert_at_tail(Node(2))
    assert dll.length == 2
    assert dll.head.data == 1
    assert dll.tail.data == 2

    dll.insert_at_head(Node(3))
    dll.insert_at_tail(Node(4))
    assert dll.length == 4
    assert dll.head.data == 3
    assert dll.tail.data == 4

    dll.insert_at_head(Node(5))
    dll.insert_at_tail(Node(6))
    assert dll.length == 6
    assert dll.head.data == 5
    assert dll.tail.data == 6

    assert str(dll) == "5 <-> 3 <-> 1 <-> 2 <-> 4 <-> 6"


def test_doubly_linked_list_insert_at_index():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.insert_at_index(Node(1), 1)

    dll.insert_at_head(Node(1))
    with pytest.raises(IndexError):
        dll.insert_at_index(Node(2), 2)

    dll.insert_at_index(Node(2), 0)
    assert dll.length == 2
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.insert_at_index(Node(3), 1)
    assert dll.length == 3
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.insert_at_index(Node(4), 2)
    assert dll.length == 4
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.insert_at_index(Node(5), 3)
    assert dll.length == 5
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.insert_at_index(Node(6), 4)
    assert dll.length == 6
    assert dll.head.data == 2
    assert dll.tail.data == 1

    assert str(dll) == "2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 1"


def test_doubly_linked_list_remove_at_head():
    dll = DoublyLinkedList()
    dll.remove_at_head()

    dll.insert_at_head(Node(1))
    assert dll.length == 1
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.remove_at_head()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None

    dll.insert_at_head(Node(1))
    dll.insert_at_head(Node(2))
    assert dll.length == 2
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.remove_at_head()
    assert dll.length == 1
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.remove_at_head()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None


def test_doubly_linked_list_remove_at_tail():
    dll = DoublyLinkedList()
    dll.remove_at_tail()

    dll.insert_at_head(Node(1))
    assert dll.length == 1
    assert dll.head.data == 1
    assert dll.tail.data == 1

    dll.remove_at_tail()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None

    dll.insert_at_head(Node(1))
    dll.insert_at_head(Node(2))
    assert dll.length == 2
    assert dll.head.data == 2
    assert dll.tail.data == 1

    dll.remove_at_tail()
    assert dll.length == 1
    assert dll.head.data == 2
    assert dll.tail.data == 2

    dll.remove_at_tail()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None


def test_doubly_linked_list_remove_at_head_and_tail():
    dll = DoublyLinkedList()
    dll.insert_at_head(Node(1))
    dll.insert_at_tail(Node(2))
    assert dll.length == 2
    assert dll.head.data == 1
    assert dll.tail.data == 2

    dll.remove_at_head()
    dll.remove_at_tail()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None

    dll.insert_at_head(Node(1))
    dll.insert_at_tail(Node(2))
    dll.insert_at_head(Node(3))
    dll.insert_at_tail(Node(4))
    assert dll.length == 4
    assert dll.head.data == 3
    assert dll.tail.data == 4

    dll.remove_at_head()
    dll.remove_at_tail()
    assert dll.length == 2
    assert dll.head.data == 1
    assert dll.tail.data == 2

    dll.remove_at_head()
    dll.remove_at_tail()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None


def test_doubly_linked_list_remove_at_index():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.remove_at_index(0)

    dll.insert_at_head(Node(1))
    with pytest.raises(IndexError):
        dll.remove_at_index(1)

    dll.remove_at_index(0)
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None

    dll.insert_at_head(Node(1))
    dll.insert_at_head(Node(2))
    dll.insert_at_head(Node(3))
    dll.insert_at_head(Node(4))
    dll.insert_at_head(Node(5))
    assert dll.length == 5
    assert dll.head.data == 5
    assert dll.tail.data == 1

    dll.remove_at_index(0)
    assert dll.length == 4
    assert dll.head.data == 4
    assert dll.tail.data == 1

    dll.remove_at_index(3)
    assert dll.length == 3
    assert dll.head.data == 4
    assert dll.tail.data == 2

    dll.remove_at_index(1)
    assert dll.length == 2
    assert dll.head.data == 4
    assert dll.tail.data == 2

    assert str(dll) == "4 <-> 2"


def test_doubly_linked_list_get_at_index():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.get_at_index(0)

    dll.insert_at_head(Node(1))
    with pytest.raises(IndexError):
        dll.get_at_index(1)

    assert dll.get_at_index(0) == 1

    dll.insert_at_head(Node(2))
    dll.insert_at_head(Node(3))
    dll.insert_at_head(Node(4))
    dll.insert_at_head(Node(5))
    assert dll.length == 5
    assert dll.head.data == 5
    assert dll.tail.data == 1

    assert dll.get_at_index(0) == 5
    assert dll.get_at_index(1) == 4
    assert dll.get_at_index(2) == 3
    assert dll.get_at_index(3) == 2
    assert dll.get_at_index(4) == 1


def test_doubly_linked_list_get_length():
    dll = DoublyLinkedList()
    assert dll.length == 0

    dll.insert_at_head(Node(1))
    assert dll.length == 1

    dll.insert_at_head(Node(2))
    dll.insert_at_head(Node(3))
    dll.insert_at_head(Node(4))
    dll.insert_at_head(Node(5))
    assert dll.length == 5


def test_doubly_linked_list_print_list_reverse():
    dll = DoublyLinkedList()
    assert dll.get_list_reverse() == ""

    dll.insert_at_head(Node(1))
    assert dll.get_list_reverse() == "1"

    dll.insert_at_head(Node(2))
    dll.insert_at_head(Node(3))
    dll.insert_at_head(Node(4))
    dll.insert_at_head(Node(5))
    assert dll.get_list_reverse() == "1 <-> 2 <-> 3 <-> 4 <-> 5"


def test_doubly_linked_list():
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_head(node)
    doubly_linked_list.insert_at_head(node2)
    doubly_linked_list.insert_at_head(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1")

    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    doubly_linked_list.insert_at_tail(node)
    doubly_linked_list.insert_at_tail(node2)
    doubly_linked_list.insert_at_tail(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1 <-> 1 <-> 2 <-> 3")
    assert(doubly_linked_list.length == 6)

    doubly_linked_list.remove_at_tail()
    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1 <-> 1 <-> 2")
    assert(doubly_linked_list.length == 5)

    doubly_linked_list.remove_at_head()
    assert(str(doubly_linked_list) == "2 <-> 1 <-> 1 <-> 2")
    assert(doubly_linked_list.length == 4)

    doubly_linked_list.remove_at_index(1)
    assert(str(doubly_linked_list) == "2 <-> 1 <-> 2")
    assert(doubly_linked_list.length == 3)

    doubly_linked_list.remove_at_index(2)
    assert(str(doubly_linked_list) == "2 <-> 1")
    assert(doubly_linked_list.length == 2)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "1")
    assert(doubly_linked_list.length == 1)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "")
    assert(doubly_linked_list.length == 0)

    doubly_linked_list.insert_at_head(node)
    doubly_linked_list.insert_at_head(node2)
    doubly_linked_list.insert_at_head(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1")
    assert(doubly_linked_list.length == 3)

    doubly_linked_list.remove_at_index(1)
    assert(str(doubly_linked_list) == "3 <-> 1")
    assert(doubly_linked_list.length == 2)

    doubly_linked_list.remove_at_index(1)
    assert(str(doubly_linked_list) == "3")
    assert(doubly_linked_list.length == 1)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "")
    assert(doubly_linked_list.length == 0)

    doubly_linked_list.insert_at_head(node)
    doubly_linked_list.insert_at_head(node2)
    doubly_linked_list.insert_at_head(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1")
    assert(doubly_linked_list.length == 3)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "2 <-> 1")
    assert(doubly_linked_list.length == 2)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "1")
    assert(doubly_linked_list.length == 1)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "")
    assert(doubly_linked_list.length == 0)

    doubly_linked_list.insert_at_head(node)
    doubly_linked_list.insert_at_head(node2)
    doubly_linked_list.insert_at_head(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1")
    assert(doubly_linked_list.length == 3)

    doubly_linked_list.remove_at_index(2)
    assert(str(doubly_linked_list) == "3 <-> 2")
    assert(doubly_linked_list.length == 2)

    doubly_linked_list.remove_at_index(1)
    assert(str(doubly_linked_list) == "3")
    assert(doubly_linked_list.length == 1)

    doubly_linked_list.remove_at_index(0)
    assert(str(doubly_linked_list) == "")
    assert(doubly_linked_list.length == 0)

    doubly_linked_list.insert_at_head(node)
    doubly_linked_list.insert_at_head(node2)
    doubly_linked_list.insert_at_head(node3)

    assert(str(doubly_linked_list) == "3 <-> 2 <-> 1")
    assert(doubly_linked_list.length == 3)

    doubly_linked_list.remove_at_index(2)
    assert(str(doubly_linked_list) == "3 <-> 2")
    assert(doubly_linked_list.length == 2)

    doubly_linked_list.remove_at_index(1)
    assert(str(doubly_linked_list) == "3")
    assert(doubly_linked_list.length == 1)
