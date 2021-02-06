class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for a in nums:
                if a & (1 << i): 
                    count += 1
                
            ans |= ((count %3) << i)

        return self.convert(ans)
    
    # address the overflow
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x
        
        
Approach 2:        
# Consider the following operations:
# 0 ^ x = x,

# x ^ x = 0；

# x & ~x = 0,

# x & ~0 =x;

# if x appears once, a=x, b=0;
# if x appears twice, a=0,b=x;
# if x appears triple, a=0,b=0;
# Therefore, the first case correponds to the single number, a will be the answer.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0 
        b = 0
        for i in nums:
            a = (a ^ i) & ~b
            b = (b ^ i) & ~a
        return a
        
        
        
        
        
