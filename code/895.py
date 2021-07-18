class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.freq2num = defaultdict(list)
        self.indx = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        count = self.freq[x]
        self.freq2num[count].append(x)
        if self.indx < self.freq[x]:
            self.indx += 1
            
    def pop(self) -> int:
        num = self.freq2num[self.indx].pop()
        self.freq[num] -= 1
        if not self.freq2num[self.indx]:
            del self.freq2num[self.indx]
            self.indx -= 1
        return num
