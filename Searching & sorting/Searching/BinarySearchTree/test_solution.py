from .solution import Build_Tree


numbers = [1, 4, 10, 20, 9, 23, 18, 34]
numbers_tree = Build_Tree(numbers)
print("Input numbers:", numbers)
print("Min:", numbers_tree.Find_Minimum_Node())
print("Max:", numbers_tree.Find_Maximum_Node())
print("Sum:", numbers_tree.calculate_Sum_Of_Nodes())
print("In order traversal:", numbers_tree.In_Order_Traversal())
print("Pre order traversal:", numbers_tree.Pre_Order_Traversal())
print("Post order traversal:", numbers_tree.Post_Order_Traversal())
