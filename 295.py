# Time O(logn)
# Space O(n)

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        large, small = self.heaps
        heapq.heappush(large, -heapq.heappushpop(small, -num))
        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

    def findMedian(self) -> float:
        large, small = self.heaps
        if len(large) < len(small):
            return -small[0]
        
        return (large[0] - small[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
