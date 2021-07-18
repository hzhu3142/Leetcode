class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p = 0
        q = m^n
        while q:
            p += 1
            q >>= 1
        return (m >> p) << p
        
   
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        
        return m << p        
        
        
