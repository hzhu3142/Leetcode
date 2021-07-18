#207
class Solution:

		def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        dependency = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            dependency[b].append(a)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = set()
        while queue:
            num = queue.popleft()
            visited.add(num)
            for depend in dependency[num]:
                indegree[depend] -= 1
                if indegree[depend] == 0:
                    queue.append(depend)

        return len(visited) == numCourses

# 210
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        dependency = defaultdict(set)
        for a, b in prerequisites:
            dependency[b].add(a)
            indegree[a] += 1

        queue = deque([course for course in indegree if not indegree[course]])
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)
            for i in dependency[course]:
                indegree[i] -= 1
                if not indegree[i]:
                    queue.append(i)

        return res if len(res) == len(indegree) else []
