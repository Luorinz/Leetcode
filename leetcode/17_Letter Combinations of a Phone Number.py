# medium


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.



class Solution:
    def dfs(self,dic,res,num,digits,ans):
        if num == len(digits) :
            res.append(ans)
            return
        letters = dic[int(digits[num])]
        for i in letters:
            temp = ans
            temp_num = num
            temp += i
            temp_num+=1
            self.dfs(dic,res,temp_num,digits,temp)
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" or not digits.isnumeric():
            return[]
        
        dic = {0:[],1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],
        6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

        res = []
        num = 0
        ans = ""
        self.dfs(dic,res,num,digits,ans)
        return res
        

t = Solution()
print(t.letterCombinations("6324"))