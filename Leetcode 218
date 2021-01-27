class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for l, r, height in buildings:
            points.append([l, height])
            points.append([r, -height])
            
        points.sort(key = lambda x: (x[0], -x[1]))
        heap = [0]
        heapq.heapify(heap)
        res = []
        for x, height in points:
            if height > 0:
                if height > -heap[0]:
                    res.append([x, height])
                heapq.heappush(heap, -height)
            else:
                heap.remove(height)
                heapq.heapify(heap)
                if -height > - heap[0]:
                    res.append([x, -heap[0]])
        
        return res
