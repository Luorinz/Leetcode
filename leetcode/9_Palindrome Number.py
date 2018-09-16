#Easy
""" Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string? """

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #My solution beat 32.56%

        if x<0:
            return False
        if x<10:
            return True
        x = str(x)
        left = 0
        right  = len(x) -1
        while left <right:
            if x[left]!= x[right]:
                return False
            
            left+=1
            right-=1
        return True


        #bese solution
        #return str(x) == str(x)[::-1]
