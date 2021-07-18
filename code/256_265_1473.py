#256
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        preCosts = [0, 0, 0]
        for i, (r, b, g) in enumerate(costs):
            curCosts = [0, 0, 0]
            for j in range(0, 3):
                curCosts[j] = costs[i][j] + min(preCosts[(j + 1) % 3], preCosts[(j + 2) % 3])
            preCosts = curCosts

        return min(preCosts)

#265
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        preCosts = costs[0]
        for i in range(1, m):
            curCosts = [0] * n
            min1 = min(preCosts)
            indx = preCosts.index(min1)
            min2 = min(preCosts[:indx]+preCosts[indx+1:])
            for j in range(n):
                if j != indx:
                    curCosts[j] = min1 + costs[i][j]
                else:
                    curCosts[j] = min2 + costs[i][j]
            preCosts = curCosts
        return min(preCosts)


#1473
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(i, k, p):
            if i == m and k == target: return 0
            if i >= m or k > target: return inf

            res = inf
            if houses[i]:
                res = min(res, dfs(i + 1, k + (houses[i] != p), houses[i]))
            else:
                for c in range(1, n + 1):
                    res = min(res, cost[i][c - 1] + dfs(i + 1, k + (c != p), c))
            return res

        res = dfs(0, 0, None)
        return res if res < inf else -1