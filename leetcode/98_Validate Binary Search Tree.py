# medium

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, node_list):
        """Form a inorder list of nodes, should be in ascending order for BST"""
        if not root:
            return
        self.helper(root.left, node_list)
        node_list.append(root.val)
        self.helper(root.right, node_list)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # Create node list
        node_list = []
        self.helper(root, node_list)
        # Check if the node list is in ascending order
        for i in range(1,len(node_list)):
            if node_list[i-1] >= node_list[i]:
                return False
            
        return True

        