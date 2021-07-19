#269
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = {letter:0 for word in words for letter in word}
        dependency = defaultdict(set)
        for m, n in zip(words[:-1], words[1:]):
            for a, b in zip(m, n):
                if a != b:
                    if b not in dependency[a]:
                        indegree[b] += 1
                        dependency[a].add(b)
                    break
            else:
                if len(m) > len(n):
                    return ''

        queue = deque([letter for letter in indegree.keys() if indegree[letter] == 0])

        res = ''
        while queue:
            letter = queue.pop()
            res += letter
            for l in dependency[letter]:
                indegree[l] -= 1
                if not indegree[l]:
                    queue.append(l)

        return res if len(res) == len(indegree) else ''

#1203
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group2items = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group2items[group[i]].append(i)

        itemIndegree, itemDependency = defaultdict(int), defaultdict(set)
        groupIndegree, groupDependency = defaultdict(int), defaultdict(set)

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    itemIndegree[i] += 1
                    itemDependency[j].add(i)
                else:
                    if group[i] not in groupDependency[group[j]]:
                        groupDependency[group[j]].add(group[i])
                        groupIndegree[group[i]] += 1

        sortGroup = self.topologicalSort([i for i in range(m)], groupIndegree, groupDependency)

        res = []
        for i in sortGroup:
            items = group2items[i]
            sortItems = self.topologicalSort(items, itemIndegree, itemDependency)
            if len(sortItems) != len(items):
                return []

            res += sortItems

        return res if len(res) == n else []

    def topologicalSort(self, items, indegree, dependency):
        queue = deque([i for i in items if not indegree[i]])

        res = []
        while queue:
            num = queue.popleft()
            res.append(num)
            for i in dependency[num]:
                indegree[i] -= 1
                if not indegree[i]:
                    queue.append(i)

        return res if len(res) == len(items) else []
