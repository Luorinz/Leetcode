# hard


# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Example 1:

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# Example 2:

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# Follow up:

# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, node_list):
        if root is None:
            return None
        self.helper(root.left, node_list)
        node_list.append(root)
        self.helper(root.right, node_list)
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # check input
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        
        # build the node list
        node_list = []
        self.helper(root, node_list)
        
        # check the switch
        # There's two cases, if two adjacent nodes are swapped, the exception occurs only once, swap the two nodes.
        # If two non-adjacent nodes are swapped, the exception occurs twice, swap the first one of the first exception and the second one of the second exception
        
        has_found_first = False
        has_found_second = False

        for i in range(1, len(node_list)):
            if node_list[i].val <= node_list[i-1].val:
                if has_found_first is False:
                    first = i - 1
                    has_found_first = True
                else:
                    if has_found_second is False:
                        second = i
                        has_found_second = True
        if has_found_second is False:
            second = first + 1
        
        # Swap two elements
        temp = node_list[second].val
        node_list[second].val = node_list[first].val
        node_list[first].val = temp
        
                
                
                
                
                
                
        