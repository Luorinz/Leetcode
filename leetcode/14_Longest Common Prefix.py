""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z. """

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # My solution

        if not strs:
            return ""
        
        length = len(strs)
        if length == 1 :
            return strs[0]

        temp = strs[0]
        i = 1
        while i < length:
            for k in range(len(strs[i])):
                if k< len(temp):
                    if strs[i][k] != temp[k] :
                        temp =temp[:k]
                else:
                    temp = temp[:k]
            i+=1
        return temp





   
                



test = Solution()
print(test.longestCommonPrefix(["aa","a"]))