Approach 1: two pointers
# 1. sort(nums)
# 2. l= 0 r=1
# 3. move pointers:
#        1. l == r or diff < K: move r++
#        2. diff > K : r++
#        3. diff == K: l+++++++ unitil diff value, res++

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # List item 3 in the text
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result
        
        
Approach 2:
# 1. k < 0
# 2. k = 0
# 3. k > 0: set(nums)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            dic = Counter(nums)
            res = 0
            for i in dic:
                if dic[i] >= 2:
                    res += 1
            return res
        if k > 0:
            m = set(nums)
            res = 0
            for i in m:
                if i+k in m:
                    res += 1
            return res
