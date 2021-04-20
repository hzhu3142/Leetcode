class Solution:
    def decodeString(self, s: str) -> str:
        curNum, curString = 0, ''
        bracket = 0
        for i, c in enumerate(s):
            if not bracket:
                if c.isdigit():
                    curNum = curNum * 10 + int(c)
                if c.isalpha():
                    curString += c
            if c == '[':
                if not bracket:
                    bracket_indx = i
                bracket += 1
                
             
            if c == ']':
                bracket -= 1
                if not bracket:
                
                    curString += curNum * self.decodeString(s[bracket_indx+1:i])         
                    curNum = 0
        return curString
