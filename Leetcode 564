class Solution:

    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        maxStr = 10 ** size + 1
        minStr = 10 ** (size - 1) - 1
        if abs(maxStr - int(n)) > abs(minStr - int(n)):
            res = str(minStr)
        else:
            res = str(maxStr)
            
        isOdd = size & 1
        preHalf = n[:(size)//2+isOdd]
        
        for i in (-1, 0, 1):
            temp = str(int(preHalf) + i)
            if isOdd:
                closestStr = temp + temp[:-1][::-1]
            else:
                closestStr = temp + temp[::-1]
            
            if closestStr == n:
                continue
                
            if abs(int(res) - int(n)) > abs(int(closestStr) - int(n)):
                res = closestStr
        
        return res
            
