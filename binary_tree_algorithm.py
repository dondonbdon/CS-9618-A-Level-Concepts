# Create a class TreeNode which has 3 variables inside the constructor method, left, value and right.
# Takes variable value as a parameter only
# write code for to traverse the binary tree using inorder, preorder and postorder
class TreeNode:

    # Constructor Method
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    # Method insert() will insert an object into the binary tree at its correct position.
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    # Method inorder() will traverse the binary tree inorderly.
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.value)
        if self.right is not None:
            self.right.inorder()


    # Method preorder() will traverse the binary tree preorderly.
    def preorder(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    

    # Method postorder() will traverse the binary tree postorderly.
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.value)


    # Method find() will traverse the tree looking for the parameter value...
    # ...returning True(Found) or False(Not Found)
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


# Create a tree with a value 60
# Insert values 19, 12, 35, 79, 56, 33, 45, 129,87 in that order
tree = TreeNode(60)
tree.insert(19)
tree.insert(12)
tree.insert(35)
tree.insert(79)
tree.insert(56)
tree.insert(33)
tree.insert(45)
tree.insert(129)
tree.insert(87)

# What is tree traversal you may ask yourself?
# Traversal is basically a way in which you can go through the data within an object in this case a binary tree.
# A proper definition would be, tree traversal is a form of graph traversal and refers to the...
# ...process of visiting each node in a tree data structure, exactly once.
# You can traverse a binary tree in 3 main ways:
# 1. Inorder traversal - Inorder goes to the most left node and prints the values in ascending order
# 2. Preorder Traversal - Preorder traversal is used to create a copy of the tree. Preorder traversal is also...
# ...used to get prefix expressions on an expression tree.
# 3. Postorder Traversal - Postorder traversal is also useful to get the postfix expression of an expression tree
print('_________________________\nINORDER ORDER TRAVERSAL\n')
tree.inorder()
print('_________________________\nPRE ORDER TRAVERSAL\n')
tree.preorder()
print('_________________________\nPOST ORDER TRAVERSAL\n')
tree.postorder()
print('_________________________\nFIND\n')


# Test data to check if the find() function is working using values 10, 12, 35
# expected results for 10, 12, 35 are False, True, True respectively.
# False meaning the value is not there
# True meaning the value is there
# print out values
print(tree.find(10))
print(tree.find(12))
print(tree.find(35))
