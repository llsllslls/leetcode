"""
求最小路径和（动态规划）
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
] 从左上角到右下角，只能向右或者向下
先建立一个和这个矩阵维度相同的0矩阵。
然后从[0][0]开始计算每个网格的最小路径和，填入val中。计算到最后一个就是解。
"""
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        val = [[0]*n for i in range(m)]
        def iter(x,y,grid):
            if x ==0 and y ==0:
                val[0][0] = grid[0][0]
            elif x ==0:
                val[x][y] = grid[x][y] +val[x][y-1]
            elif y ==0:
                val[x][y] = grid[x][y] + val[x-1][y]
            else:
                val[x][y] = grid[x][y] + min(val[x-1][y],val[x][y-1])
        for i in range(m):
            for j in range(n):
                iter(i,j,grid)
        return val[m-1][n-1]





if __name__ =="__main__":
    s=Solution()
    print(s.minPathSum([[1,2,5],[3,2,1]]))
