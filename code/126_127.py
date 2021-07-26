#word ladder I
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset, wordgraph, queue = set(wordList), defaultdict(set), deque([(beginWord, 1)])
        if endWord not in wordset:
            return 0
        while queue:
            word, step = queue.popleft()
            if word not in wordgraph:
                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        newword = word[:i] + ch + word[i + 1:]
                        if ch == word[i]:
                            continue
                        if newword in wordset:
                            wordgraph[word].add(newword)
            if word == endWord:
                return step
            else:
                for newword in wordgraph[word]:
                    queue.append((newword, step + 1))
                wordgraph[word] = set()
        return 0
#word ladder II
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset, queue, worddis, wordgraph = set(wordList), deque([(beginWord, 1)]), {beginWord : 1}, defaultdict(set)
        res, length = [], inf
        if endWord not in wordset:
            return []
        while queue and queue[0][1] < length:
            word, step = queue.popleft()
            if word not in wordgraph:
                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        if ch == word[i]:
                            continue
                        newword = word[:i] + ch + word[i + 1:]
                        if newword in wordset:
                            wordgraph[word].add(newword)
            for nextword in wordgraph[word]:
                if nextword not in worddis:
                    worddis[nextword] = step + 1
                elif nextword in worddis and worddis[nextword] < step + 1:
                    continue
                if nextword == endWord:
                    length = step + 1
                else:
                    queue.append((nextword, step + 1))
        if length == inf:
            return []

        def backtracking(path, curword):
            if worddis[curword] < len(path):
                return
            if curword == endWord:
                res.append(path[:])
                return
            for nextword in wordgraph[curword]:
                path.append(nextword)
                backtracking(path, nextword)
                path.pop()

        backtracking([beginWord], beginWord)

        return res

# the method 2 below is much lower than the method 1;
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        path_q = deque([[beginWord]])
        visited = set([beginWord])
        visit_pending = set()
        res = []
        level = 1
        length = len(beginWord)
        while path_q:
            curr_path = path_q.popleft()
            if len(curr_path) > level:
                level += 1
                visited.update(visit_pending)
                visit_pending = set()
            word = curr_path[-1]
            for i in range(length):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word in wordList and new_word not in visited:
                        new_path = curr_path + [new_word]
                        visit_pending.add(new_word)
                        if new_word == endWord:
                            res.append(new_path)
                        else:
                            path_q.append(new_path)

        return res
