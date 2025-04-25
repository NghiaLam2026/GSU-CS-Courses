#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 03/24/2024 @ 11:59PM

class TreeNode: #This class represents each node in the binary tree
    def __init__(self, val): #Initialize the TreeNode with a value, and left and right children as None
        if val == "":
            raise ValueError("TreeNode must be initialized with a value!")
        self.val = val
        self.left = None
        self.right = None

def pre_order(root): #Visit root, then left, then right
    if root is None: #If the current node is None, end the recursion
        return []
    if root:
        print(root.val, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def in_order(root): #Visit left, root, then right
    if root is None: #If the current node is None, end the recursion
        return []
    
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)

def post_order(root): #Visit left, right, then root
    if root is None: #If the current node is None, end the recursion
        return []
    
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=" ")


# Normal Binary Tree Test Case
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print("Sample Test Case: ")
print("Pre-order Traversal: ", end = "")
pre_order(root)
print("\nIn-order Traversal: ", end="")
in_order(root)
print("\nPost-order Traversal: ", end="")
post_order(root)
print("\n") 
# Normal Binary Tree Test Case


#Full Binary Tree Test Case
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Full Binary Tree Traversals:")
print("Pre-order Traversal: ", end="")
pre_order(root)
print("\nIn-order Traversal: ", end="")
in_order(root)
print("\nPost-order Traversal: ", end="")
post_order(root)
print("\n")
#Full Binary Tree Test Case


#Dominantly Left Tree Test Case
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
print("Left-skewed Binary Tree Traversals:")
print("Pre-order Traversal: ", end="")
pre_order(root)
print("\nIn-order Traversal: ", end="")
in_order(root)
print("\nPost-order Traversal: ", end="")
post_order(root)
print("\n")
#Dominantly Left Tree Test Case


#Dominantly Right Tree Test Case
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print("Right-skewed Binary Tree Traversals:")
print("Pre-order Traversal: ", end="")
pre_order(root)
print("\nIn-order Traversal: ", end="")
in_order(root)
print("\nPost-order Traversal: ", end="")
post_order(root)
print("\n")
#Dominantly Right Tree Test Case