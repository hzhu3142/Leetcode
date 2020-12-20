class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        
        i = 0
        while left + i < len(nums) and nums[left+i] == target:
            i += 1
            
        return [left, left+i-1]
