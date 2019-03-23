#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.52%)
# Total Accepted:    179.9K
# Total Submissions: 676.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # find the length first, then handle k
    # On time O1 space
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
        # relink the linked list
        temp.next = head
        k %= length
        # Handle edge case
        if k != 0:
            for i in range(length - k):
                temp = temp.next
        res = temp.next
        temp.next = None
        return res
        
        

