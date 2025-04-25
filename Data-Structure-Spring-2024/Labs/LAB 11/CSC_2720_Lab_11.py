#Nghia Lam
#CSC 2720 Lab 014
#Lab time: 2:15 PM
#Due time: 03/31/2024 @ 11:59PM

from collections import deque

class TreeNode:
    def __init__ (self, val):
        self.val = val # Node value
        self.left = None # Pointer to the left child
        self.right = None #Pointer to the right child

def level_order_traversal(root):
    if not root:
        return [] # Return an empty list for an empty tree
    
    result = "" # Initialize an empty string to hold the traversal results
    queue = deque([root]) # Use a deque as a queue to support O(1) popleft operation

    while queue: # While there are nodes to process in the queue
        node = queue.popleft() # Remove and return the leftmost node int he queue
        result += str(node.val) + " " # Add the node value to the result string with a space

        if node.left: # If the node has a left child, add it to the queue for later processing
            queue.append(node.left)
        if node.right: # If the noed ahs a right child, add it to the queue for later processing
            queue.append(node.right)

    return result.strip()

#NORMAL TEST CASE
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(level_order_traversal(root), "\n")
#NORMAL TEST CASE



#EMPTY TREE TEST CASE
root = None
print(level_order_traversal(root), "\n")
#EMPTY TREE TEST CASE



#LEFT-SKEWED TREE TEST CASE
root = TreeNode(12)
root.left = TreeNode(10)
root.left.left = TreeNode(8)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(4)
print(level_order_traversal(root), "\n")
#LEFT-SKEWED TREE TEST CASE



#RIGHT-SKEWED TREE TEST CASE
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(5)
print(level_order_traversal(root))
#RIGHT-SKEWED TREE TEST CASE