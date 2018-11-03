# medium


# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        
        # find the mid list node
        slow_ptr = fast_ptr = prev = head
        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next
        
        
        # make new tree root
        root = TreeNode(slow_ptr.val)
        
        # cut the current list
        right_ptr = slow_ptr.next
        prev.next = None
        
        #Adjust:
        if slow_ptr == fast_ptr:
            root.right = TreeNode(right_ptr.val)
        else:
            # make root's left and right
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(right_ptr)
        
        return root
        