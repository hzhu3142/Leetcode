# BFS Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def setParent(root, parent = None):
            if root:
                root.parent = parent
                setParent(root.left, root)
                setParent(root.right, root)
                
        setParent(root)
        if K == 0:
            return [target.val]
        step = 0
        visited = set([target.val])
        curLevel = [target]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                for new in (node.left, node.right, node.parent):
                    if new and new.val not in visited:
                        visited.add(new.val)
                        nextLevel.append(new)
                    
            step += 1
            if step == K:
                return [i.val for i in nextLevel]
            curLevel = nextLevel
            
        return []


#DFS Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.map = {}
        self.ans = []
        self.findTarget(root, target)
        self.dfs(root, target, K, self.map[root])
        return self.ans
    
    # to build the self.map
    def findTarget(self, root, target):
        if not root:
            return -1
        
        if root == target:
            self.map[root] = 0
            return 0
        
        left = self.findTarget(root.left, target)
        if left >= 0:
            self.map[root] = left + 1
            return left + 1
        
        right = self.findTarget(root.right, target)
        if right >= 0:
            self.map[root] = right + 1
            return right + 1
        
        return -1
    
    # to build the self.ans
    def dfs(self, root, target, K, distance):
        if not root:
            return
        
        if root in self.map:
            distance = self.map[root]
            
        if distance == K:
            self.ans.append(root.val)
            
        self.dfs(root.left, target, K, distance + 1)
        self.dfs(root.right, target, K, distance + 1)

