class Excel:

    def __init__(self, height: int, width: str):
        self.array = [[[0, None]] * (ord(width) - ord('A') + 1) for _ in range(height + 1)]
        print(self.array)

    def set(self, row: int, column: str, val: int) -> None:
        self.array[row][ord(column) - ord('A')] = [val, None]

    def get(self, row: int, column: str) -> int:
        if not self.array[row][ord(column) - ord('A')][1]:
            return self.array[row][ord(column) - ord('A')][0]
        
        return self.sum(row, column, self.array[row][ord(column) - ord('A')][1])

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.array[row][ord(column) - ord('A')] = [0, numbers]
        res = 0
        for p in numbers:
            if ':' in p:
                res += self.subtotal(p)
            else:
                r, c = int(p[1:]), p[0]
                res += self.get(r, c)
        return res

    def subtotal(self, formula):    
        num1, num2 = formula.split(':')
        r1, c1 = int(num1[1:]), ord(num1[0])
        r2, c2 = int(num2[1:]), ord(num2[0])
        res = 0
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                res += self.get(r, chr(c))
        return res
