class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            area = self. LargestRectangleArea(heights)
            res = max(res, area)
        
        return res
    
    def LargestRectangleArea(self, heights):
        stack = [-1]
        heights += [0]
        res = 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                hig = heights[stack.pop()]
                res = max(res, (i - stack[-1] - 1) * hig)
            
            stack.append(i)
        
        return res
