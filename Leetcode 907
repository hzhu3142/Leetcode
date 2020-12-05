class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [1] * len(arr)
        
        for i, v in enumerate(arr):
            while stack and stack[-1][1] >= v:
                res[i] += res[stack[-1][0]]
                stack.pop()
            stack.append((i, v))     
        stack = []
        res1 = [1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1][1] > arr[i]:
                res1[i] += res1[stack[-1][0]]
                stack.pop()
            stack.append((i, arr[i]))
            
        for i, v in enumerate(arr):
            res[i] = res[i] * res1[i] * v
    
        return sum(res) % (10**9+7)
