class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k:
                stack.pop()
                k -= 1
            stack.append(i)  
        return "".join(stack[:len(stack)-k]).lstrip("0") or "0"
