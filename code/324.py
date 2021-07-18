class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = (len(nums)+1)//2 
        nums[::2],nums[1::2] = nums[:n][::-1], nums[n:][::-1]
        
        
        
#quick selections + virtual index
import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid = (n+1)//2
        
        def quickSort():
            start, end = 0, n-1
            while True:
                pivot = nums[random.randint(start, end)]
                l = cur = start
                r = end
                while cur <= r:
                    if nums[cur] < pivot:
                        nums[l], nums[cur] = nums[cur], nums[l]
                        l += 1
                        cur += 1
                    elif nums[cur] > pivot:
                        nums[cur], nums[r] = nums[r], nums[cur]
                        r -= 1
                    else:
                        cur += 1
            
                if nums[mid-1] == pivot:
                    return 
                elif r+1 > mid:
                    end = r - 1
                elif r+1 < mid:
                    start = r + 1
        
       
        quickSort()
        # print(nums)

        
        # nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
        # virtual index
        mapIdx=lambda i:(1+2*i)%(n|1)
        i,j,k=0,n-1,0
        while k<=j:
            if nums[mapIdx(k)]>mid:
                nums[mapIdx(k)],nums[mapIdx(i)]=nums[mapIdx(i)],nums[mapIdx(k)]
                i+=1
                k+=1
            elif nums[mapIdx(k)]<mid:
                nums[mapIdx(k)],nums[mapIdx(j)]=nums[mapIdx(j)],nums[mapIdx(k)]
                j-=1
            else:
                k+=1  
