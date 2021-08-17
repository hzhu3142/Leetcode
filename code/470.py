class Solution:
    def rand10(self):
        rand40 = 40
        while rand40 >= 40:
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1