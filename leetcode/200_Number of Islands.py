# medium

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    def bfs(self,grid,m,n):
        if grid[m][n] == "0":
            return False
        qm = [m]
        qn = [n]

        dm = [1,0,0,-1]
        dn = [0,1,-1,0]
        while qm != []:
            temp_m = qm.pop(0)
            temp_n = qn.pop(0)
            for i in range(4):
                cur_m = temp_m+dm[i]
                cur_n = temp_n+dn[i]
                if 0<=cur_m<len(grid) and 0<= cur_n < len(grid[0]) and grid[cur_m][cur_n] != "0":
                    qm.append(cur_m)
                    qn.append(cur_n)
                    grid[cur_m][cur_n] = "0"
        return True


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        is_found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                is_found = self.bfs(grid,i,j)
                if is_found:
                    res+=1
        return res




t = Solution()
t1= [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(t.numIslands(t1))