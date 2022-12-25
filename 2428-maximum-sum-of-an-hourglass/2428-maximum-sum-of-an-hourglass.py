class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        maxSum=0        
        for i in range(R-2):
            for j in range(C-2):
                sum= grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1]+ grid[i+2][j]+ grid[i+2][j+1] + grid[i+2][j+2] 
                maxSum=max(sum,maxSum)
        return maxSum
        