# 198
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                dp[0][1] = num
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + num

        return max(dp[-1])

#213
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, nums):
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        for i, num in enumerate(nums):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = num
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = dp[i - 1][0] + num

        return max(dp[-1])

#337
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return (0, 0)

            left= helper(root.left)
            right= helper(root.right)

            doRob = left[0] + right[0] + root.val
            noRob = max(left) + max(right)

            return (noRob, doRob)
        return max(helper(root))

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