# 314
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
        
# 987
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dic = defaultdict(list)
        
        def helper(root, x, y):
            if not root:
                return 
            dic[(x, y)].append(root.val)
            
            helper(root.left, x+1, y-1)
            helper(root.right, x+1, y+1)
        
        helper(root, 0, 0)
        position = sorted(dic, key = lambda x: (x[1], x[0]))
        res = []
        pre_y = -inf
        for x, y in position:
            if y == pre_y:
                res[-1].extend(sorted(dic[x, y]))
            else:
                res.append(sorted(dic[x, y]))
            pre_y = y      
        return res        
        
        
