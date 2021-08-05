# BFS
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        list1 = set([s])
        valid = set()
        while list1:
            list2 = set()
            for parentheses in list1:
                if self.check(parentheses):
                    valid.add(parentheses)
                    continue

                for i, letter in enumerate(parentheses):
                    if letter not in '()':
                        continue
                    newString = parentheses[:i] + parentheses[i+1:]
                    list2.add(newString)
            if valid:
                return valid
            list1 = list2


    def check(self, string):
        count = 0
        for ch in string:
            if ch == '(':
                count += 1
            elif ch ==')':
                count -= 1

            if count < 0:
                return False

        return count == 0
