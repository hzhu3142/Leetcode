class Solution(object):
    def numIslands(self, grid):
        islands = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'
            move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for a, b in move:
                dfs(a + i,b + j)   
        
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
