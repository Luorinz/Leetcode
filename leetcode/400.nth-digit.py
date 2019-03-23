#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.09%)
# Total Accepted:    44.7K
# Total Submissions: 148.4K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution_1:
    # On solution
    # TLE
    def findNthDigit(self, n: int) -> int:
        # Count from 1 to n
        temp = 1
        digits = 1
        while n > digits:
            # Each time minus the total digits of cur num
            n -= digits
            # cur num + 1
            temp += 1
            # Redefine the total digits of cur num
            digits = len(str(temp))
        return int(str(temp)[n-1])

class Solution:
    # O logn time
    def findNthDigit(self, n: int) -> int:
        # temp means the first number of digit n
        temp = 1
        digits = 1
        step = 9
        # 1 digit: 1-9 1*9=9chars
        # 2 digits: 10-99 2*90=180chars
        # 3 digits: 100-999 3*900=2700chars
        # Ologn time to find digits
        while n > digits * step:
            # reduce n
            n -= digits * step
            digits += 1
            step *= 10
            temp *= 10
        # temp+(n-1)//digits means finding the current number
        # (n-1)%digits means finding the current digits
        # O logn space to store the string
        return int((str(temp + (n - 1)// digits))[(n-1) % digits])

        

        