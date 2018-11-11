# medium

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Check input
        if root is None:
            return []
        # Use BFS to read through the node level by level
        ans = []
        level = [root]
        while level:
            temp_ans = []
            temp_level = []
            for i in level:
                # Add all nodes to ans in current level
                temp_ans.append(i.val)
                # Generate a list of all nodes of next level
                for j in [i.left, i.right]:
                    if j is not None:
                        temp_level.append(j)
            ans.append(temp_ans)
            level = temp_level
        return ans
        