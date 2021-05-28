class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        height = 0
        visited = set()
        heap = []
        for i in range(m):
            for j in range(n):
                if i in (0, m-1) or j in (0, n-1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
                    
        res = 0
        while heap:
            h, x, y = heapq.heappop(heap)
            height = max(height, h)
            for a, b in [(x+1,y), (x, y+1), (x-1, y), (x, y-1)]:
                if a < 0 or a >= m or b < 0 or b >= n:
                    continue
                if (a, b) in visited:
                    continue
                
                res += max(0, height - heightMap[a][b])
                heapq.heappush(heap, (heightMap[a][b], a, b))
                visited.add((a, b))
                
        return res
