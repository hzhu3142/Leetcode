class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.smaller = [0] * len(nums)
        self.mergelist(list(enumerate(nums)))
        return self.smaller
    
    def mergelist(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        l = self.mergelist(nums[:mid])
        r = self.mergelist(nums[mid:])
        return self.mergesort(l, r)     
        
    def mergesort(self, l, r):
        if not l or not r:
            return l or r
        result = []
        m, n = len(l), len(r)
        i = j = 0
        while i < m or j < n:
            if j == n or i < m and l[i][1] <= r[j][1]:
                self.smaller[l[i][0]] += j
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        result += l[i:] + r[j:]
        return result
