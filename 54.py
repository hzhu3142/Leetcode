class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] <= h:
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    j, m = stack.pop()
                    res = max(res, (i - j) * m)
                stack.append((j, h))
        
        while stack:
            j, m = stack.pop()
            res = max(res, (len(heights)-j) * m)
        
        return res
