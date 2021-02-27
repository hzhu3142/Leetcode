# 647

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0
        
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                self.res += 1
                i -= 1
                j += 1
        
        for i in range(n):
            helper(i, i)
            helper(i, i+1)
        
        return self.res
        
#730

#Approach 1:

class Solution: Botteom Up
    
    def countPalindromicSubsequences(self, S: str) -> int:
        dp = [[0] * len(S) for _ in range(len(S))]
        for length in range(1, len(S) + 1):
            for start in range(len(S) - length + 1):
                for c in "abcd":
                    try:
                        left = S.index(c, start, start + length)
                        right = S.rindex(c, start, start + length)
                        if left == right:
                            dp[start][start + length - 1] += 1
                        else:
                            dp[start][start + length - 1] += dp[left + 1][right - 1] + 2
                    except:
                        pass
                    
        return dp[0][-1] % 1000000007
   
#Approach 2: Top Down

class Solution:

    def countPalindromicSubsequences(self, S: str) -> int:
        @lru_cache(None)
        def dfs(s, e):
            if s >= e:
                return 0
            res = 0
            for c in 'abcd':
                if c in S[s:e]:
                    i = S[s:e].index(c)
                    j = S[s:e].rindex(c)
                    res += dfs(s + i + 1, s + j) + 2 if i != j else 1
            return res % (10**9 + 7)
                
        return dfs(0, len(S))
        
        
        
        
        
        
