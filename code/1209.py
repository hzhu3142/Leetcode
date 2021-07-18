class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, ch in enumerate(s):
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
            
        print(stack)
        return ''.join([x * y for x, y in stack])
