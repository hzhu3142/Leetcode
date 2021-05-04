 #139
  class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        print(dp)
        return dp[-1]
      
      
#140
#approach 1 backtracking
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        res = []
        def backtracking(indx, path):
            if indx == len(s):
                res.append(path[1:])
                return res
            
            for i in range(indx+1, len(s)+1):
                if s[indx:i] in wordset:
                    backtracking(i, path+' '+s[indx:i])
        
        backtracking(0, '')
        return res
				
#approach 2: DFS + memo
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        
        @lru_cache(None)
        def helper(indx):
            if indx == len(s):
                return ['']
            res = []
            for i in range(indx+1, len(s)+1):
                if s[indx:i] in wordset:
                    for rest in helper(i):
                        if rest:
                            res.append(s[indx:i] + ' ' + rest)
                        else:
                            res.append(s[indx:i])
            return res
        
        return helper(0)
 
#472
#Approach 1 trie
# It is very easy to get TLE when using trie, but the code below can pass.
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for i, c in enumerate(word):
            node = node.children[c]
            if node.isWord:
                if self.exists(word[i+1:]):
                    return False
                else:
                    continue
        node.isWord = True
        return True
    
    def exists(self, word):
        node = self.root
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
                if node.isWord:
                    if i == len(word)-1 or self.exists(word[i+1:]):
                        return True
                    else:
                        continue
            else:
                return False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        trie = Trie()
        res = []
        words = sorted(words, key=len)
        for word in words:
            if not trie.insert(word):
                res.append(word)
        
        
        return res
	
	#Approach 2 DFS + recursion
	class Solution:
	
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        
        @lru_cache(None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res
#Approach 3 word break I template.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        preWords = set()
        words.sort(key = len)
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)
        
        return res
    
    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False
        
        dp = [False] * (len(string) + 1)
        dp[0] = True
        
        for i in range(len(string)+1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]
