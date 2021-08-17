import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        res = float('-inf')

        for x, y in points:

            # pop out the elements where heap[0][1] - x > k
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                total = -heap[0][0] + y + x
                res = max(res, total)

            heapq.heappush(heap, (x - y, x))
        return res