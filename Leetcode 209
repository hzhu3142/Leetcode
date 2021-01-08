# Binary search
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        presum = [0] * len(nums)
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] = presum[i-1] + nums[i]
            
        res = inf
        for i in range(len(nums)):
            if i == 0:
                indx = bisect.bisect_left(presum, s)
            else:
                indx = bisect.bisect_left(presum, s+presum[i-1])
            
            if indx < len(nums):
                res = min(res, indx - i + 1)
            
        return res if res != inf else 0
        
   
  # two pointers
  class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = 0
        left = 0
        res = inf
        for i in range(len(nums)):
            total += nums[i]
            while total >=s:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1
        return res if res != inf else 0
