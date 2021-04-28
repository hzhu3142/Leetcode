class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        weeks = len(days[0])
        cities = len(days)
        
        @lru_cache(None)
        def helper(i, preCity):
            if i == weeks:
                return 0
            
            res = 0
            for city in range(cities):
                if preCity == city or flights[preCity][city]:
                    res = max(res, helper(i+1, city) + days[city][i])
            return res
        return helper(0, 0)
          
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        weeks = len(days[0])
        cities = len(days)
        dp = [[-inf] * cities for _ in range(weeks+1)]
        dp[0][0] = 0
        for i in range(1, weeks+1):
            for j in range(cities):
                for preCity in range(cities):
                    if j == preCity or flights[preCity][j]:
                        dp[i][j] = max(dp[i][j], dp[i-1][preCity] + days[j][i-1])
        
        return max(dp[-1])
      
      
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        weeks = len(days[0])
        cities = len(days)
        dp = [[0] * cities for _ in range(weeks+1)]
        for i in range(weeks-1, -1, -1):
            for j in range(cities):
                for nextCity in range(cities):
                    if j == nextCity or flights[j][nextCity]:
                        dp[i][j] = max(dp[i][j], dp[i+1][nextCity] + days[nextCity][i])
        
        return dp[0][0]  
          
          
          
          
          
          
