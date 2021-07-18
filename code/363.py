class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            prefix = [0, inf]
            preSum = 0
            rslt = -inf
            for i, num in enumerate(arr):
                preSum += num
                indx = bisect.bisect_left(prefix, preSum - k)
                rslt = max(rslt, preSum - prefix[indx])
                bisect.insort(prefix, preSum)
            
            return rslt
                
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        
        res = -inf
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = []
                for x in range(m):
                    arr.append(matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0))
                
                res = max(res, maxSumSubarray(arr))
        
        return res
