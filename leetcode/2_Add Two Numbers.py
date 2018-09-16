#Medium
""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #My solution
        #beat 25.40%
        num1 = 0
        num2 = 0
        num3 = 0
        
       
        
        # get num1
        i = 1
        while l1:
            num1 += l1.val *i 
            i*=10
            l1 = l1.next
        print(num1)
        # get num2
        k = 1
        while l2:
            num2 += l2.val *k 
            k*=10
            l2 = l2.next     
        print(num2)
        # create num3 and return 
        num3 = num1+num2
        num3 = str(num3)
        pre = ListNode(0)
        head = pre
        for i in num3[::-1]:
            temp = ListNode(int(i))
            pre.next = temp
            pre = pre.next
        
        return head.next        
        
        #Best solution
"""         if not l1 or not l2: return l1 or l2
        head = l1
        n = 0
        while l1 and l2:
            d = l1.val + l2.val + n
            n,d = d >= 10,d%10
            l1.val = d
            cur,l1,l2 = l1,l1.next,l2.next
        cur.next = l1 or l2
        while n:
            if not cur.next:
                cur.next = ListNode(0+n)
                break
            else:
                d = cur.next.val + n
                n,cur.next.val = d >= 10,d%10
                cur = cur.next
        return head         """