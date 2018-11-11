# mediun


# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution:
    def helper(self, i, j, board, word):
        # Check edge case
        # All letters are checked
        if word == "":
            return True
        # Across the border
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        # Avoid duplicate
        temp = board[i][j]
        board[i][j] = '#'
        # DFS rescursion
        res = self.helper(i + 1, j, board, word[1:]) or \
            self.helper(i, j + 1, board, word[1:]) or \
            self.helper(i - 1, j, board, word[1:]) or \
            self.helper(i, j - 1, board, word[1:])
        # Retrieve current letter
        board[i][j] = temp
        return res
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Use DFS to solve this problem
        if board is None or board == []:
            return False
        # To every item in the board, use dfs to search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(i, j, board, word):
                    return True
        return False