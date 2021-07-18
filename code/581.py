#Approach 1: sort time O(nlogn) space O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(nums)
        
        l = inf
        
        for i in range(n):
            if arr[i] != nums[i]:
                l = i
                break
        
        if l == inf:
            return 0
        
        for i in range(n-1, -1, -1):
            if arr[i] != nums[i]:
                r = i
                break
        
        return r - l + 1

#Approach 2: monotonic stack time O(n) space O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l, mx = inf, -inf
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                indx = stack.pop()
                l = min(l, indx)
                mx = max(mx, nums[indx])
            stack.append(i)
        
        if l == inf:
            return 0
        
        r = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < mx:
                r = i
                break
        
        return r-l+1
      
      
   # Approach 3: not sort time O(n) space O(1)
  
  class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find right limit of the subarray. Traverse array from left to right
        r = 0
        big = nums[0]
        for i in range(len(nums)):
            if nums[i] >= big: 
                big = nums[i]                
            else:
                r = i
        
        if r == 0:
            return 0
        
        # Find left limit of the subarray. Traverse array from right to left

        l = 0
        small = nums[-1]
        for i in reversed(range(len(nums))):
            if nums[i] <= small: 
                small = nums[i]
            else:
                l = i
        
        return r - l + 1
