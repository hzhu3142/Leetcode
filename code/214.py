# pythonic
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s)-1, -1, -1):
            if s[:i+1]==s[:i+1][::-1]:
                return s[i+1:][::-1]+s

# Iteration
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n <= 1: 
            return s
        
        maxLen, i = 1, 0
        while i < n/2:
         
            l, r = i, i
            while r < n - 1 and s[r] == s[r + 1]: 
                r += 1
            
            i = r + 1
            while r < n - 1 and l and s[r + 1] == s[l - 1]:  
                r = r + 1 
                l = l - 1
            
            if l == 0: 
                maxLen = r + 1
        
        return s[maxLen:][::-1] + s


# recursion
class Solution:
    def shortestPalindrome(self, s: str) -> str:
    
        if not s or len(s) == 1: return s
        j = 0   
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1        
        return s[j:][::-1] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]
        
# KMP
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        a = s + '*' + s[::-1]
        m = self.getPattern(a)
        return s[m:][::-1] + s
        
        
    def getPattern(self, a: str) -> str:    
        n = len(a)
        pattern = [-1] * n
        i = 0
        j = 1
        while j < n:
            if a[i] == a[j]:
                pattern[j] = i
                i += 1
                j += 1
            elif i > 0:
                i = pattern[i - 1] + 1
            else:
                j += 1
        
        return pattern[-1] + 1


# Robin-Karp
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        maxLen = -1
        base = 1
        h1 = 0
        h2 = 0
        for i in range(len(s)):
            h1 = (h1 * 26 + ord(s[i]) - ord('a'))
            h2 = (h2 + (ord(s[i]) - ord('a')) * base)
            if h1 == h2:
                maxLen = i + 1
            base *= 26
        
        return s[maxLen:][::-1]+s
