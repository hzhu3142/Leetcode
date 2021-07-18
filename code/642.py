class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        cur = self.root
        for l in word:
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur["*"] = word

    def search(self, prefix, cur = None):
        if not cur:
            cur = self.root
        for l in prefix:
            if l not in cur:
                return []
            cur = cur[l]
        
        res = []
        for l in cur:
            if l == "*":
                res.append(cur[l])
            else:
                res += self.search('', cur[l])
        return res

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.lookUp = {}
        for i, c in enumerate(sentences):
            self.lookUp[c] = times[i]
        self.trie = Trie()
        for c in sentences:
            self.trie.insert(c)
        self.keyword = ""
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.lookUp[self.keyword] = self.lookUp.get(self.keyword, 0) + 1
            self.trie.insert(self.keyword)
            self.keyword = ""
            return []
        
        self.keyword += c
        lst = self.trie.search(self.keyword)
        lst.sort(key = lambda x: (-self.lookUp[x], x))
        return lst[:3]
