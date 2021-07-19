#227
class Solution:

    def calculate(self, s: str) -> int:
        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y
        }

        stack = []
        preOperator = '+'
        num = 0
        for i, ch in enumerate(s + '+'):
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/' and preOperator in '+-':
                stack.append(operator[preOperator](0, num))
                num = 0
                preOperator = ch
            elif ch in '+-*/' and preOperator in '*/':
                preNum = stack.pop()
                stack.append(operator[preOperator](preNum, num))
                num = 0
                preOperator = ch

        return sum(stack)

#224
# For this approach, it is like add '+( )' in the outside of the input, so the signs is initialized as [1, 1].

class Solution:

    def calculate(self, s: str) -> int:
        total = 0
        i, signs = 0, [1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total

# 772
class Solution:
    def calculate(self, s: str) -> int:
        # 2 stacks
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif c in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = c, 0
        return sum(stack)
