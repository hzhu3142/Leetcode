
#200
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


#305
class DSU:
    def __init__(self):
        self.parents = {}
        self.count = 0

    def setParent(self, x):
        self.parents[x] = x
        self.count += 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)
        self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU()
        res = []
        for x, y in positions:
            if (x, y) in dsu.parents:
                res.append(dsu.count)
                continue
            dsu.setParent((x, y))
            for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (a, b) in dsu.parents and not dsu.connected((x, y), (a, b)):
                    dsu.union((x, y), (a, b))

            res.append(dsu.count)
        print(dsu.parents)
        return res
