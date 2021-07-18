class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while 0 < n <= len(nums):
                tmp = nums[n-1]
                nums[n-1] = float('inf')
                n = tmp
        
        for i in range(len(nums)):
            if nums[i] != float('inf'):
                return i+1
            
        return len(nums)+1
