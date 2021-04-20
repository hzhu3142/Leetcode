class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            nonflip = dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            flip = dfs(root1.right, root2.left) and dfs(root1.left, root2.right)
            
            return nonflip or flip
        
        return dfs(root1, root2)
