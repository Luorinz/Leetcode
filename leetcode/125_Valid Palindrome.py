# esay

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Check edge case
        if s is None:
            return False
        # Preprocessing
        s = s.strip().lower()
        if s == "":
            return True
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string += i
        # Use double pointers to check palindrome
        left = 0
        right = len(new_string) - 1
        while left < right and new_string[left] == new_string[right]:
            left += 1
            right -= 1
        return left >= right
                