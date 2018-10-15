# easy

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

# Note:

# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        res = []
        l = len(A)
        ind = 0
        for i in range(l):
            if A[i] % 2 == 1:
                if ind % 2 == 1:
                    if odd == []:
                        res.append(A[i])
                        ind+=1
                    else:
                        odd.append(A[i])
                        res.append(odd.pop())
                        ind+=1
                else:
                    odd.append(A[i])
                    if even != []:
                        res.append(even.pop())
                        ind+=1
                # print(odd,even,res)
            else:
                if ind % 2 == 0:
                    if even == []:
                        res.append(A[i])
                        ind+=1
                    else:
                        res.append(even.pop())
                        even.append(A[i])
                        ind+=1
                else:
                    even.append(A[i])
                    if odd!= []:
                        res.append(odd.pop())
                        ind+=1
                # print(odd,even,res)
        if even == [] and odd == []:
            return res
        else:
            while even!= [] or odd != []:
                if res == []:
                    res.append(even.pop())
                if res[-1] % 2 ==1:
                    res.append(even.pop())
                else:
                    res.append(odd.pop())
            return res