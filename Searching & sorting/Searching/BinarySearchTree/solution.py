class Binary_Search_Tree:

    # Constructor with vaue we are going to insert in tree with assigning left and right child with default None
    def __init__(self, data):
        self.data = data
        self.Left_child = None
        self.Right_child = None

    def Add_Node(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.Left_child:
                self.Left_child.Add_Node(data)
            else:
                self.Left_child = Binary_Search_Tree(data)

        else:
            if self.Right_child:
                self.Right_child.Add_Node(data)
            else:
                self.Right_child = Binary_Search_Tree(data)

    def Find_Node(self, val):
        # If current node is equal to data we are finding return true
        if self.data == val:
            return True

        if val < self.data:
            if self.Left_child:
                return self.Left_child.Find_Node(val)
            else:
                return False

        if val > self.data:
            if self.Right_child:
                return self.Right_child.Find_Node(val)
            else:
                return False

    def In_Order_Traversal(self):
        elements = []
        if self.Left_child:
            elements += self.Left_child.In_Order_Traversal()

        elements.append(self.data)

        if self.Right_child:
            elements += self.Right_child.In_Order_Traversal()

        return elements

    def Post_Order_Traversal(self):
        elements = []
        if self.Left_child:
            elements += self.Left_child.Post_Order_Traversal()
        if self.Right_child:
            elements += self.Right_child.Post_Order_Traversal()

        elements.append(self.data)

        return elements

    def Pre_Order_Traversal(self):
        elements = [self.data]
        if self.Left_child:
            elements += self.Left_child.Pre_Order_Traversal()
        if self.Right_child:
            elements += self.Right_child.Pre_Order_Traversal()

        return elements

    def Find_Maximum_Node(self):
        if self.Right_child is None:
            return self.data
        return self.Right_child.Find_Maximum_Node()

    def Find_Minimum_Node(self):
        if self.Left_child is None:
            return self.data
        return self.Left_child.Find_Minimum_Node()

    def calculate_Sum_Of_Nodes(self):
        left_sum = self.Left_child.calculate_Sum_Of_Nodes() if self.Left_child else 0
        right_sum = self.Right_child.calculate_Sum_Of_Nodes() if self.Right_child else 0
        return self.data + left_sum + right_sum


def Build_Tree(elements):
    root = Binary_Search_Tree(elements[0])

    for i in range(1, len(elements)):
        root.Add_Node(elements[i])

    return root
