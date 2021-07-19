#371
# recursion + bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        if b == 0:
            return a
        if b & mask == 0:
            return (a & mask)
        return self.getSum(a^b, (a&b)<<1)

# Iteration
class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_digits = math.floor(math.log2(max(abs(a), abs(b)))) + 2
        mask = 2 ** (bit_digits + 1) - 1
        while b:
            if b & mask == 0:
                return (a & mask)
            c = a & b
            a ^= b
            b = c << 1
        return a

#50
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x

        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)

        i = 0
        res = 1
        temp = x
        while (1 << i) <= n:
            if n & (1 << i):
                res *= temp
            temp *= temp
            i += 1

        return res

#recursion
class Solution:
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1

        if n < 0:
            return self.myPow(1/x, -n)

        if n & 1:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)

#43
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
        

#29
# The use of abs in Python (and other arbitrary-precision integer languages) needs to be considered carefully,
# because abs(-2**31) = 2**31, which is outside the allowed range by 1.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:   # overflow case
            return 2**31 - 1

        sign = 1
        if (dividend > 0) ^ (divisor > 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                multiple <<= 1
                temp <<= 1
            res += multiple
            dividend -= temp
        return res * sign
