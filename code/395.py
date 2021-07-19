class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack = [s]
        res = 0
        while stack:
            substring = stack.pop()
            for i in set(substring):
                if substring.count(i) < k:
                    stack.extend([m for m in substring.split(i)])
                    break
            else:
                res = max(res, len(substring))

        return res
