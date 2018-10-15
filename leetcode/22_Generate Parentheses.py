# medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:

    def dfs(self,n,left_num,right_num,cur,ans):
        if right_num > left_num :
            return
        if right_num == n and left_num == n:
            if cur not in ans:
                ans.append(cur)
            return
        temp = cur
        left = left_num
        right = right_num
        if left_num < n:
            temp += "("
            left+=1
            self.dfs(n,left,right_num,temp,ans)

        temp2 = cur
        if right_num < n :
            temp2 += ")"
            right += 1
            self.dfs(n,left_num,right,temp2,ans)
        # print(cur)

        


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0 :
            return []
        res = []
        left_num = 0
        right_num = 0
        ans = []
        cur = ""
        self.dfs(n,left_num,right_num,cur,ans)
        return ans


        

t = Solution()
print(t.generateParenthesis(2))