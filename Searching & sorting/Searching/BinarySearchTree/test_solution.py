from .solution import Build_Tree
import pytest

print(pytest)

numbers = [1, 4, 10, 20, 9, 23, 18, 34]
Ans = sorted(numbers)


def test_sorted_node():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.In_Order_Traversal() == Ans


def test_min_ofnode():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.Find_Minimum_Node() == Ans[0]


def test_max_ofnode():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.Find_Maximum_Node() == Ans[-1]


def test_sum_ofnode():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.calculate_Sum_Of_Nodes() == sum(Ans)


def test_post_order():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.Post_Order_Traversal() == [9, 18, 34, 23, 20, 10, 4, 1]


def test_pre_order():
    numbers_tree = Build_Tree(numbers)
    assert numbers_tree.Pre_Order_Traversal() == [1, 4, 10, 9, 20, 18, 23, 34]
