# medium

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Use double pointers to solve this problem
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            # To avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Find the solutions of a + b = -c
            # Transfer it to two sum problem
            # The solution is double pointers
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # Avoid the duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return ans