# medium

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #DP Solution
        dp = [True] + [False] * len(s)
        for i in range(1,len(dp)):
            for word in wordDict:
                l = len(word)
                if i - l >= 0 and dp[i - l] == True and s[i-l:i] in wordDict:
                    dp[i] = True
        return dp[-1]

        
        
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s1 = "applepenapple"
wordDict2 = ["apple", "pen"]

t = Solution()
print(t.wordBreak(s,wordDict))
print(t.wordBreak(s1,wordDict2))