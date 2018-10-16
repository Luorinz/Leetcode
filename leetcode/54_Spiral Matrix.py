# medium


# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        ind = 0
        try:
            while matrix != [] and matrix != [[]]:
                if ind % 4 == 0:
                    res += matrix[0]
                    matrix.pop(0)
                elif ind % 4 == 1:
                    j = -1
                    for i in matrix:
                        res.append(i[j])
                        i.pop()
                    
                elif ind % 4 == 2:
                    res += matrix[-1][::-1]
                    matrix.pop()
                elif ind % 4 == 3:
                    j = 0
                    for i in matrix[::-1]:
                        res.append(i[0])
                        i.pop(0)
                ind+=1
        except IndexError:
            return res
        return res
                    
            
                


        
test =  [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
test1 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
test3 = [[7],[9],[6]]
test4 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
t = Solution()
print(t.spiralOrder(test))
print(t.spiralOrder(test1))
print(t.spiralOrder(test3))
print(t.spiralOrder(test4))