#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.30%)
# Total Accepted:    194.5K
# Total Submissions: 687.4K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Check if the num is in the right place. By deafult nums[i] = i+1
            # If not in the right place, swap it until it is
            # Caution: Never use tuple exchange in a list!!!
            # nums[i] > 0 means don't have to take action to negative
            # nums[i] <= len(nums) means the num isn't out of range
            # nums[i] != nums[nums[i]-1] means the num isn't in the right place
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        return len(nums) + 1

        

