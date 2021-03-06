#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (53.52%)
# Total Accepted:    180.3K
# Total Submissions: 336.4K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#
class Solution:
    # hashmap
    # O n + klogk time
    # O
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        # On time On space
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        # O klogk time, k for num of distinct nums, O k space
        temp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # O k time
        return [temp[i][0] for i in range(k)]

