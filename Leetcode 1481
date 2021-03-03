class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num2freq = Counter(arr)
        freq2num = defaultdict(list)
        
        for num, freq in num2freq.items():
            freq2num[freq].append(num)
            
        n = len(arr)
        for freq in range(1, n+1):
            if k < freq:
                break
            while freq2num[freq] and k >= freq:
                num = freq2num[freq].pop()
                del num2freq[num]
                k -= freq
        
        return len(num2freq)
    

#Approach 2:
    
class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        s = sorted(arr,key = lambda x:(c[x],x))
        return len(set(s[k:]))
