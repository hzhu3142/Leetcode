# 131
Time: O(N* 2^N)
Space: O(N)
#Approach1: DFS
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path+[s[:i]], res)

#Approach 2	
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.dfs(s, {})
    
    def dfs(self, s, memo):
        if s in memo:
            return memo[s]
        
        memo[s] = []
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                if i + 1 == len(s):
                    memo[s].append([s])
                else:
                    for rest in self.dfs(s[i+1:], memo):
                        memo[s].append([s[:i+1]] + rest)
        
        return memo[s]
        
# 132

#XXXX [iXXj] XXXX
#0123  4567  89AB
class Solution:

    def minCut(self, s: str) -> int:
        cut = [x for x in range(-1,len(s))] #cut[i] for s[:i]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]
