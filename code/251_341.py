Leetcode 341

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            data = self.stack.pop().getList()
            self.stack += data[::-1]
        return self.stack
        
Leetcode 251

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.stack = v[::-1]

    def next(self) -> int:
        while self.stack and not isinstance(self.stack[-1], int):
            data = self.stack.pop()
            self.stack += data[::-1]
        
        return self.stack.pop()

    def hasNext(self) -> bool:
        while self.stack and not isinstance(self.stack[-1], int):
            data = self.stack.pop()
            self.stack += data[::-1]
        return self.stack
