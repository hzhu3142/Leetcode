class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:

        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        m = len(targetPath)

        # dp[i][j] -> the minimum distance of the targetPath for targetPath[:i+1] ending with city j
        dp = [[m] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = int(targetPath[0] != names[i])

        prevOptimalCity = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for c in range(n):
                for preC in graph[c]:
                    if dp[i - 1][preC] < dp[i][c]:
                        dp[i][c] = dp[i - 1][preC]
                        prevOptimalCity[i][c] = preC
                dp[i][c] += (names[c] != targetPath[i])

        min_distance = m + 1
        cityIndx = None
        for i in range(n):
            if min_distance > dp[-1][i]:
                min_distance = dp[-1][i]
                cityIndx = i

        # print(dp)

        res = [cityIndx]
        for i in range(m - 1, 0, -1):
            city = prevOptimalCity[i][res[-1]]
            res.append(city)

        return res[::-1]