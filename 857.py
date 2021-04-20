# ratio = wage/quality -> increasing
#  money = sum(ratio*quality) -> maxheap

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([float(w/q), q] for w, q in zip(wage, quality))
        heap = []
        res = inf
        totalQuality = 0
        for ratio, qual in workers:
            heapq.heappush(heap, -qual)
            totalQuality += qual
            if len(heap) > K:
                totalQuality += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, ratio * totalQuality)
        
        return res
