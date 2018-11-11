# easy


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # Double pointers

        ptr_1 = 0
        ptr_2 = 0
        while ptr_2 < n:
            if nums1[ptr_1] < nums2[ptr_2]:
                if ptr_1 >= m + ptr_2:
                    nums1[ptr_1] = nums2[ptr_2]
                    ptr_1 += 1
                    ptr_2 += 1
                else:
                    ptr_1 += 1
            else:
                nums1.insert(ptr_1, nums2[ptr_2])
                nums1.pop()
                ptr_2 += 1
                ptr_1 += 1
