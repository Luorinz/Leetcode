#Medium
""" Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring. """

#My solution
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        temp = ""
        i = 0
        while i < len(s):
            if s[i] not in dic:
                dic[s[i]] = i
                temp += s[i]
            else:
                
                dic[s[i]] = i




test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))