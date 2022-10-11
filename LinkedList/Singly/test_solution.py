from .solution import LinkedList, Node
import pytest


def test_get_length():
    ll = LinkedList()
    assert(ll.get_length() == 0)
    ll.insert_at_head(Node(1))
    assert(ll.get_length() == 1)
    ll.insert_at_tail(Node(2))
    assert(ll.get_length() == 2)
    ll.insert_at_index(Node(3), 1)
    assert(ll.get_length() == 3)
    ll.remove_at_head()
    assert(ll.get_length() == 2)
    ll.remove_at_tail()
    assert(ll.get_length() == 1)
    ll.remove_at_index(0)
    assert(ll.get_length() == 0)


def test_insert_at_head():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    assert(ll.get_at_index(2) == 1)
    ll.print_list()


def test_insert_at_tail():
    ll = LinkedList()
    ll.insert_at_tail(Node(1))
    ll.insert_at_tail(Node(2))
    ll.insert_at_tail(Node(3))
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 1)
    assert(ll.get_at_index(1) == 2)
    assert(ll.get_at_index(2) == 3)
    ll.print_list()


def test_insert_at_index():
    ll = LinkedList()
    ll.insert_at_index(Node(1), 0)
    assert(ll.get_length() == 1)
    assert(ll.get_at_index(0) == 1)
    ll.insert_at_index(Node(2), 1)
    assert(ll.get_length() == 2)
    assert(ll.get_at_index(0) == 1)
    assert(ll.get_at_index(1) == 2)
    ll.insert_at_index(Node(3), 1)
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 1)
    assert(ll.get_at_index(1) == 3)
    assert(ll.get_at_index(2) == 2)
    ll.print_list()


def test_remove_at_head():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    ll.remove_at_head()
    assert(ll.get_length() == 2)
    assert(ll.get_at_index(0) == 2)
    assert(ll.get_at_index(1) == 1)
    ll.print_list()


def test_remove_at_tail():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    ll.remove_at_tail()
    assert(ll.get_length() == 2)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    ll.print_list()


def test_remove_at_index():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    ll.remove_at_index(1)
    assert(ll.get_length() == 2)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 1)
    ll.print_list()


def test_get_at_index():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    assert(ll.get_at_index(2) == 1)
    assert(ll.get_at_index(3) is None)
    ll.print_list()


def test_print_list():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    expected = "3 -> 2 -> 1"
    assert(str(ll) == expected)


def test_linked_list_empty():
    ll = LinkedList()
    assert(ll.get_length() == 0)
    assert(ll.get_at_index(0) is None)
    ll.remove_at_head()
    assert(ll.get_length() == 0)
    ll.remove_at_tail()
    assert(ll.get_length() == 0)

    with pytest.raises(IndexError):
        ll.remove_at_index(0)

    assert(ll.get_length() == 0)
    ll.print_list()


def test_linked_list_one():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    assert(ll.get_length() == 1)
    assert(ll.get_at_index(0) == 1)
    ll.remove_at_head()
    assert(ll.get_length() == 0)
    ll.remove_at_tail()
    assert(ll.get_length() == 0)

    with pytest.raises(IndexError):
        ll.remove_at_index(0)

    assert(ll.get_length() == 0)
    ll.print_list()


def test_linked_list_two():
    ll = LinkedList()
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    assert(ll.get_at_index(2) == 1)
    ll.print_list()


def test_linked_list():
    ll = LinkedList()
    assert(ll.get_length() == 0)
    ll.insert_at_head(Node(1))
    assert(ll.get_length() == 1)
    ll.insert_at_tail(Node(2))
    assert(ll.get_length() == 2)
    ll.insert_at_index(Node(3), 1)
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 1)
    assert(ll.get_at_index(1) == 3)
    assert(ll.get_at_index(2) == 2)
    ll.remove_at_head()
    assert(ll.get_length() == 2)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    ll.remove_at_tail()
    assert(ll.get_length() == 1)
    assert(ll.get_at_index(0) == 3)
    ll.remove_at_index(0)
    assert(ll.get_length() == 0)
    ll.insert_at_head(Node(1))
    ll.insert_at_head(Node(2))
    ll.insert_at_head(Node(3))
    assert(ll.get_length() == 3)
    assert(ll.get_at_index(0) == 3)
    assert(ll.get_at_index(1) == 2)
    assert(ll.get_at_index(2) == 1)
    ll.print_list()
