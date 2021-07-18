#bottom up
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [list] * len(nums)
        res = []
        for i in range(len(nums)):
            temp = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(temp) < len(dp[j]):
                    temp = dp[j]
            dp[i] = temp[:]
            dp[i].append(nums[i])
            if len(res) < len(dp[i]):
                res = dp[i]
        return res
      
      
#top-down
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @lru_cache(None)
        def helper(i):
            res = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    temp = helper(j)
                    if len(res) < len(temp):
                        res = temp[:]
            res.append(nums[i])
            return res
        
        rslt = []
        for i in range(len(nums)):
            temp1 = helper(i)
            if len(rslt) < len(temp1):
                rslt = temp1
        
        return rslt
