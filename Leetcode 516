class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s) - 1
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            
            res = 0    
            for ch in set(s):
                i, j = s.find(ch), s.rfind(ch)
                res = max(res, 1 if i==j else 2 + dfs(s[i+1:j]))
            
            memo[s] = res
            
            return memo[s]
        return dfs(s)
				
#Approach 2:

class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        dp = [[0]*len(s) for _ in range(len(s))]
        for l in range(1, len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]+2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
