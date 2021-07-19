class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        def check(mid):
            set1 = {tuple(nums1[i:i+mid]) for i in range(m-mid+1)}
            set2 = {tuple(nums2[i:i+mid]) for i in range(n-mid+1)}
            return any(m in set2 for m in set1)


        l, r = 0, m
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1


        return r
