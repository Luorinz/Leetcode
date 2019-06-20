# easy

# ou're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.


class Solution1:
    # O(m*n) O1 space
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            if i in J:
                count +=1
        return count
    
class Solution:
    # O(m+n) time Om spacee
    def numJewelsInStones(self, J, S):
        s = set()
        for i in J:
            s.add(i)
        res = 0
        for i in S:
            if i in s:
                res += 1
        return res