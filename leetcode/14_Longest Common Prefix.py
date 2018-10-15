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
        if not strs:
            return ""
        ind = 0
        res = ""
        temp = ""
        is_start = False
        try:
            while True:
                for i in strs:
                    if is_start == False:
                        is_start = True
                        temp = i[ind]
                    else:
                        if temp != i[ind]:
                            return res
                ind+=1
                res += temp
                temp = ""
                is_start = False
        except IndexError:
            return res        
        return res     
      

test = Solution()
print(test.longestCommonPrefix(["aa","a"]))