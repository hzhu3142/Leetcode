# recursion + bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        if b == 0: 
            return a
        if b & mask == 0: 
            return (a & mask)
        return self.getSum(a^b, (a&b)<<1)
        
# Iteration    
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_digits = math.floor(math.log2(max(abs(a), abs(b)))) + 2
        mask = 2 ** (bit_digits + 1) - 1
        while b:
            if b & mask == 0:
                return (a & mask)                     
            c = a & b
            a ^= b
            b = c << 1
        return a
