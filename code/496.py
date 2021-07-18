class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
  
        dic = {v:i for i, v in enumerate(nums2)}
        res = []
        for v in nums1:
            indx2 = dic[v]
            j = 1
            while indx2+j < len(nums2):
                if nums2[indx2] < nums2[indx2+j]:
                    res.append(nums2[indx2+j])
                    break
                j += 1
                    
            
            if indx2+j == len(nums2):
                res.append(-1)
        
        return res
