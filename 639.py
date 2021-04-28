class Solution:
    def numDecodings(self, s: str) -> int:
        
        mod = 10 ** 9 + 7
        pre0, pre1, pre2 = 1, 0, 0
        for ch in s:
            if ch == '*':
                cur0 = pre0 * 9 + pre1 * 9 + pre2 * 6 
                cur1 = pre0
                cur2 = pre0
            
            else:
                cur0 = (ch > '0') * pre0 + pre1 + pre2 * (ch <= '6')
                cur1 = (ch == '1') * pre0
                cur2 = (ch == '2') * pre0
        
            pre0, pre1, pre2 = cur0 % mod, cur1, cur2
            
        return pre0
