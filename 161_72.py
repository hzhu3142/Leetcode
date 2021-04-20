# 161

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        
        if n - m > 1:
            return False
        
        for i, ch in enumerate(s):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:] == t[i:]
        
        return n - m == 1
 
 #72
 
 class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1), len(word2)
        @lru_cache(None)
        def helper(i, j):
            if i == m or j == n:
                return n - j + m - i
            
            if word1[i] == word2[j]:
                res = helper(i+1, j+1)
            else:
                res = min(helper(i+1, j+1), helper(i, j+1), helper(i+1, j))+1
            return res
        
        return helper(0, 0)
        
