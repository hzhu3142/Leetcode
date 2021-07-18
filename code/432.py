class Node:
    def __init__(self, val):
        self.val = val
        self.data = set()
        self.next = None
        self.pre = None
        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.memo = {}
        
    def add(self, node, key):
        if node.val+1 != node.next.val:
            newNode = Node(node.val+1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        newNode.data.add(key)
        return newNode
    
    def add_pre(self, node, key):
        if node.val - 1 != node.pre.val:
            newNode = Node(node.val-1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.data.add(key)
        return newNode
    
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.memo:
            self.memo[key] = self.add(self.head, key)
        else:
            node = self.memo[key]
            self.memo[key] = self.add(node, key)
            node.data.remove(key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.memo:
            node = self.memo[key]
            node.data.remove(key)
        
            del self.memo[key]
            if node.val > 1:
                self.memo[key] = self.add_pre(node, key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None
                
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.tail.pre.data:
            return ''
        num = self.tail.pre.data.pop()
        self.tail.pre.data.add(num)
        return num

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.head.next.data:
            return ''
        num = self.head.next.data.pop()
        self.head.next.data.add(num)
        return num
