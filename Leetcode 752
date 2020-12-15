class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #1. corner case: '0000' in deadends, return -1
        #2. '0000' -> 9000, 1000, 0900, 0100, 0010, 0090, 0009 0001
        #3. visited(set), depth, queue, deadends(set)
        
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        #initial
        visited = set(['0000'])
        queue = deque(['0000'])
        steps = 0
        
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr == target:
                    return steps
                for i in range(4):
                    for move in [-1, 1]:
                        new_digit = (int(curr[i]) + move) % 10
                        new_wheel = curr[:i] + str(new_digit) + curr[i+1:]
                        if new_wheel not in deadends and new_wheel not in visited:
                            queue.append(new_wheel)
                            visited.add(new_wheel)
            steps += 1
        
        return -1
