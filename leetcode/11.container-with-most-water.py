#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.90%)
# Total Accepted:    326.8K
# Total Submissions: 761.8K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution:
    # 2 ptrs
    # On time O 1 space
    def maxArea(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height)-1
        while left < right:
            # First get the cur biggest res
            h = min(height[left], height[right])
            total = max(total, (right-left)*h)
            # Get the highest point from left
            while height[left] <= h and left < right:
                left += 1
            # Get the highest point from right
            while height[right] <= h and left < right:
                right -= 1
            # Here we get the second largest height
        return total
        

