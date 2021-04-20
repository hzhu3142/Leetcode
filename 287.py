# The approach is applicable to 142. Linked List Cycle II
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        fast = nums[nums[fast]]
        slow = nums[slow]
        
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
            
        return fast
