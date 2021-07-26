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
