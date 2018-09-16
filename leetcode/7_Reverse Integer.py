#easy
""" Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume 
that your function returns 0 when the reversed integer overflows. """
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        #my solution beat 48.76%

        x = str(x)
        res = ""
        for i in x[::-1]:
            if i != '-':
                res+=i
                
        res = int(res)

        if x[0] == '-':
            res = 0-res
            
        if res < 0- 2**31 or res > 2**31 -1:
            return 0
        else:
            return res

        #best solution
"""         negative = 0

        if x < 0:
            negative = 1
            x = -(x)
    
        stf = str(x)
        revs = stf[::-1]
        revi = int(revs)
        
        if revi >= 2 ** 31:
            revi = 0
            
        if negative == 1:
            revi = -revi
        
        return(revi)        
        
 """