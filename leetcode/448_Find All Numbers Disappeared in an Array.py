# easy

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        l = len(nums)
        res = []
        lst = list(range(1,l+1))
        dic = {i:0 for i in lst}
        for i in nums:
            if i in dic:
                dic[i] += 1
        for k,v in dic.items():
            if v ==0:
                res.append(k)
        
        return res

    #Another Solution
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        whole = set(range(1,len(nums)+1))
        return list(whole - set(nums))