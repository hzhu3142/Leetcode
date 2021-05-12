#343
#Approach 1; Dp time O(n), space O(n)
class Solution:
    def integerBreak(self, n: int) -> int:     
        dp = [1] * (n + 1)
        for j in range(3, n+1):
            for i in range(1, j//2+1):
                dp[j] = max(dp[j], max((j-i), dp[j-i]) * i)
        
        return dp[-1]
				
				
#Approach 2: math Space O(1), time O(n)				
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        
        res = 0
        for i in range(2, n//2 + 1):
            num = n // i
            temp = pow(i, num)
            reminder = n % i
            if reminder:
                if reminder == 1:
                    temp = temp // i * (i + 1)
                else:
                    temp = temp * reminder
            res = max(res, temp)
        
        return res
				
	#Approach 3: math time O(1), space O(1)
	#when the prime factor is 3, the product is the maximum, because 3 is the number closest to e (2.73)

class Solution:

    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1

        num = n // 3
        reminder = n % 3
        if reminder == 0:
            return pow(3, num)
        elif reminder == 1:
            return pow(3, num-1) * 4
        elif reminder == 2:
            return pow(3, num) * 2  
          
#1808          
class Solution:
    def maxNiceDivisors(self, x):
        if x < 4:
            return x
        
        quotient, reminder = x // 3, x % 3
        
        mod = 10**9 + 7
        if reminder == 0:
            return pow(3, quotient, mod)
        elif reminder == 1: 
            return pow(3, quotient - 1, mod) * 4 % mod
        elif reminder == 2: 
            return pow(3, quotient, mod) * 2 % mod   
