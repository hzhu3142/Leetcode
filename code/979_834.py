# 979
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            self.res += abs(l) + abs(r)
            
            return l + r + root.val - 1
        
        helper(root)
        return self.res
        
        
# 834

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        count = [1] * N
        res = [0] * N
        
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
            
        def dfs(root, parent):
            for i in tree[root]:
                if i != parent:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]
        
        def dfs2(root, parent):
            for i in tree[root]:
                if i != parent:
                    res[i] = res[root] + N - count[i] - count[i]
                    dfs2(i, root)
        
        dfs(0, -1)
        dfs2(0, -1)
        return res
