class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        mini = min(cost)

        @functools.lru_cache(None)
        def dp(n):
            if target == n: return 0
            if target < n or target - n < mini: return float("-inf")

            res = float("-inf")
            for i in range(len(cost)):
                temp = dp(n + cost[i]) * 10 + i + 1
                res = max(res, temp)
            return res

        return str(max(dp(0), 0))