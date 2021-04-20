class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.val2indx = defaultdict(int)
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2indx:
            return False
        
        self.arr.append(val)
        self.val2indx[val] = self.length
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2indx:
            return False
        indx = self.val2indx[val]
        lastValue = self.arr[-1]
        self.arr[indx] = lastValue
        self.val2indx[lastValue] = indx
        self.arr.pop()
        del self.val2indx[val]
        self.length -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        indx = random.randint(0, self.length - 1)
        return self.arr[indx]
