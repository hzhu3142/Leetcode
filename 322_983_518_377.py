#322
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == inf else dp[-1]

# 983
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)

        @lru_cache(None)
        def mincost(i):
            if i > days[-1]:
                return 0

            if i not in dayset:
                return mincost(i + 1)
            res = []
            for dura, cost in zip([1, 7, 30], costs):
                spend = mincost(i + dura) + cost
                res.append(spend)

            return min(res)

        return mincost(1)
#983
class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0 for i in range(days[-1]+1)]
        for i in range(days[-1]+1):
            if i not in days:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(dp[max(0,i-1)]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
        return dp[-1]
# 983
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def mincost(i):
            if i >= len(days):
                return 0

            res = inf
            j = i
            for dura, cost in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + dura:
                    j += 1
                res = min(res, mincost(j) + cost)

            return res

        return mincost(0)

#983
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def find(d):
            return max(bisect.bisect(days, d), 0)

        n = len(days)
        dp = [0] * (n + 1)
        for i, day in enumerate(days):
            dp[i + 1] = min(dp[find(day - 1)] + costs[0], dp[find(day - 7)] + costs[1], dp[find(day - 30)] + costs[2])

        return dp[-1]


#518
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]

#377
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[-1]