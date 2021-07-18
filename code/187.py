# Approach 1: Linear_time Slice Using Substring + HashSet
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        h = defaultdict(int)
        for i in range(len(s)-9):
            h[s[i:i+10]] += 1
        
        return [i for i in h.keys() if h[i] > 1]
        
 # Approach 2: Hash rolling 
 class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        ch2int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [ch2int[ch] for ch in s]
        
        pattern = functools.reduce(lambda v, x: v * 4 + x, nums[:10], 0)
        seen = set([pattern])
        res = set()
        for i in range(10, len(s)):
            pattern = (pattern - nums[i-10] * 4 ** 9) * 4 + nums[i]
            if pattern in seen:
                res.add(s[i-9:i+1])
            seen.add(pattern)
        
        return res
        
# Approach 3: bit manipulation
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        digits = {"A": 0, "C": 1, "G": 2, "T": 3}
        mask = 0xfffff
        pattern = 0
        seen = set()
        res = set()
        for i, ch in enumerate(s):
            pattern = (pattern << 2 | digits[ch]) & mask
            
            if i >= 9:
                if pattern in seen:
                    res.add(s[i-9:i+1])
                else:
                    seen.add(pattern)
                    
        return res
        
        
