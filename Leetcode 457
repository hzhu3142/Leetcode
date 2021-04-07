class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i, num in enumerate(nums):
            g = str(i)
            while type(nums[i]) != str and num * nums[i] > 0 and nums[i] % len(nums) != 0:
                indx = i
                i = (i + nums[i]) % len(nums)
                nums[indx] = g
            
            if nums[i] == g:
                return True
            
        return False
            
