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
