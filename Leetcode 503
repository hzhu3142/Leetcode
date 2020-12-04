from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = deque()
        nums += nums
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
                
            if not stack:
                res.appendleft(-1)
            else:
                res.appendleft(stack[-1])
            stack.append(nums[i])
            
        return list(res)[:len(nums)//2]
