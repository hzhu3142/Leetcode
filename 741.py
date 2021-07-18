class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @lru_cache(None)
        def helper(x1, x2, step):
            y1 = step - x1
            y2 = step - x2
            if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
                return -inf
            
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -inf
            
            if x1 == x2 == y1 == y2 == n-1:
                return grid[-1][-1]
            
            cur = grid[x1][y1] if x1 == x2 and y2 == y2 else grid[x1][y1] + grid[x2][y2]
            nxt = -inf
            for a in [x1+1, x1]:
                for b in [x2+1, x2]:
                    nxt = max(nxt, helper(a, b, step+1))
                
            return cur + nxt
        
        return max(helper(0, 0, 0), 0)
