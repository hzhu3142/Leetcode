class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, tem in enumerate(T):
            while stack and stack[-1][1] < tem:
                tmp = stack.pop()
                res[tmp[0]] = i - tmp[0]
            stack.append((i, tem))
        
        return res
