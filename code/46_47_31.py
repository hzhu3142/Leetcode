#46
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums) - 1:
                res.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        res = []
        dfs(0)
        return res

#47
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []

        def dfs(path, used):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue

                used[i] = True
                dfs(path+[nums[i]], used)
                used[i] = False


        visited = [False] * n
        dfs([], visited)
        return res


#31
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                smal = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1] and nums[smal] > nums[j]:
                        smal = j
                nums[i-1], nums[smal] = nums[smal], nums[i-1]
                break
            i -= 1
            if i == 0:
                return nums.sort()
        nums[i:] = sorted(nums[i:])
