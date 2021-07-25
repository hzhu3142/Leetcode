# 218
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

# 218
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = set([b[0] for b in buildings] + [b[1] for b in buildings])
        q, i, res = [], 0, [[0,0]]
        points = sorted(list(points))
        for p in points:
            while i < len(buildings) and buildings[i][0] == p:
                heapq.heappush(q, (-buildings[i][2], buildings[i][1]))
                i += 1
            while q and q[0][1] <= p:
                heapq.heappop(q)
            h = -q[0][0] if q else 0
            if h != res[-1][1]:
                res.append([p, h])
        return res[1:]

# 391
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        a, b, c, d = inf, inf, -inf, -inf
        corner = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            a = min(a, x1)
            b = min(b, y1)
            c = max(c, x2)
            d = max(d, y2)
            corner ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            area += (x2 - x1) * (y2 - y1)

        return area == (c-a) * (d-b) and corner == {(a, b), (a, d), (c, b), (c, d)}


# 850
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append([y1, x1, x2, 1])
            events.append([y2, x1, x2, 0])
        events.sort()

        def sweep():
            res, cur = 0, 0
            for x1, x2 in active:
                cur = max(cur, x1)
                res += max(0, x2 - cur)
                cur = max(cur, x2)
            return res

        active, area, prey = [], 0, events[0][0]
        for y, x1, x2, status in events:
            area += sweep() * (y - prey)
            if status:
                bisect.insort(active, [x1, x2])
            else:
                active.remove([x1, x2])
            prey = y
        return area % (10 ** 9 + 7)
