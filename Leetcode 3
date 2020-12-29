class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = p = 0
        
        for i, v in enumerate(s):
            if v in dic:
                p = max(p, dic[v]+1)
            
            dic[v] = i
            res = max(res, i-p+1)
            
        return res
