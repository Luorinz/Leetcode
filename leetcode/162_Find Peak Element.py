# medium

# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None
        l = len(nums)
        if l == 1:
            return 0
        nums = [float("-inf")] + nums + [float("-inf")]
        i = 1
        res = []
        while i < l+1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1] :
                print(i-1,nums[i])
                return (i-1)
            i+=1
        return 0




nums = [1,2,1,3,5,6,4]
nums1 = [1,2]
t = Solution()
# print(t.findPeakElement(nums))
print(t.findPeakElement(nums1))