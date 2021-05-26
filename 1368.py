#DP
class Solution:
    def minCost(self, A):
        n, m, inf, k = len(A), len(A[0]), 10**9, 0
        dp = [[inf] * m for i in range(n)]
        dirt = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        bfs = []

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and dp[x][y] == inf): 
                return
            dp[x][y] = k
            bfs.append([x, y])
            a, b = dirt[A[x][y]]
            dfs(x + a, y + b)

        dfs(0, 0)
        while bfs:
            k += 1
            bfs, bfs2 = [], bfs
            for x, y in bfs2:
                for i, j in dirt[1:]:
                    dfs(x + i, y + j)
        return dp[-1][-1]
				
				
				
#dijkstra
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        move = {1:(0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}
        heap = [(0, 0, 0)]
        visited = set()
        while heap:
            cost, i, j = heapq.heappop(heap)
            if i == m-1 and j == n-1:
                return cost
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for direction in range(1, 5):
                x, y = move[direction]
                if i+x < 0 or i+x >= m or j+y < 0 or j+y >= n or (i+x, j+y) in visited:
                    continue
                heapq.heappush(heap, (cost+(direction != grid[i][j]), i+x, j+y))
