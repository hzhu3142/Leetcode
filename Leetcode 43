class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = int(num1)
        b = int(num2)
        res = 0
        k = 0
        while a:
            if a & 1:
                res += b << k
            a >>= 1
            k += 1
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(a, b):
            return a if not b else add(a ^ b, (a & b) << 1)
        
        a = int(num1)
        b = int(num2)
        res = 0
        while a:
            if a & 1:
                res = add(res, b)
            a >>= 1
            b <<= 1
        return str(res)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')
