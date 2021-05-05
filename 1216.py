#Approach 1 top-down
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        @lru_cache(None)
        def helper(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return helper(i+1, j-1)
            else:
                return min([helper(i, j-1), helper(i+1, j)]) + 1
        
        return helper(0, n-1) <= k
      
#Approach 2 bottom up

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]    
        
        for j in range(1, n):
            for i in range(j-1, -1, -1):
        
        # for i in range(n-1, -1, -1): # method 2 to do the for-loop
        #     for j in range(i+1, n):
        
        # for l in range(1, n):   # method 3 to do the for-loop
        #     for i in range(n-l):
        #         j = i + l
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        
        return dp[0][-1] <= k
      
      
