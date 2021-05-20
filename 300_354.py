#300
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        candidate = []
        for num in nums:
            indx = bisect.bisect_left(candidate, num)
            if indx == len(candidate):
                candidate.append(num)
            else:
                candidate[indx] = num
        
        print(candidate)
        return len(candidate)
        
 #354       
 class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))        
        candidate = []
        for _, num in envelopes:
            indx = bisect.bisect_left(candidate, num)
            if indx == len(candidate):
                candidate.append(num)
            else:
                candidate[indx] = num
        
        return len(candidate)   
        
        
