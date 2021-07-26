#740
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        arr = sorted(freq)
        n = len(arr)
        dp = [[0, 0] for _ in range(n)]
        for i, num in enumerate(arr):
            if i == 0:
                dp[0][1] = freq[num] * num
            else:
                if num - arr[i-1] == 1:
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = dp[i-1][0] + freq[num] * num
                else:
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = dp[i][0] + freq[num] * num
        return max(dp[-1])

#309
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool = 0
        sell = buy = -inf

        for p in prices:
            cool, sell, buy = max(cool, sell), buy + p, max(buy, cool - p)
        return max(cool, sell)
