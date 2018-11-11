# medium


# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n <=1:
            return 1
        # Use catalan number model 
        catalan = [1,1]
        for i in range(2, n+1):
            temp = 0
            for j in range(i):
                temp += catalan[i-1-j]*catalan[j]
            catalan.append(temp)
        return catalan[-1]