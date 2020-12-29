class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if(k == 1):
            return nums
        
        length = len(nums)
        res = []
        max_window = []
        
        for i in range(length):
            
            while max_window and nums[i] > nums[max_window[-1]]:
                max_window.pop()
            max_window.append(i)
            
            if i >= k-1:
                res.append(nums[max_window[0]])
                if i-k+1 == max_window[0]:
                    max_window.pop(0)
        
        return res
    
