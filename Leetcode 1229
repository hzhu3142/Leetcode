class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        n = len(nums)
        maxNum = max(nums)
        minNum = min(nums)
        bucketSize = (maxNum - minNum) // (n-1) or 1
        bucketNum = (maxNum - minNum) // bucketSize + 1
        bucket = [[inf, -inf] for _ in range(bucketNum)]
        for i, v in enumerate(nums):
            m = (v-minNum)//bucketSize
            bucket[m][0] = min(bucket[m][0], v)
            bucket[m][1] = max(bucket[m][1], v)
        
        bucket = [x for x in bucket if x[0] != inf]
        
        return max([bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket))])
