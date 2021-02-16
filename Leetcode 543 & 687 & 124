# 543
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            self.res = max(self.res, l+r+1)
            
            return max(l, r) + 1
        
        helper(root)
        return self.res - 1

#687
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 1
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            if root.left and root.left.val == root.val:
                left = l
            else:
                left = 0
            
            if root.right and root.right.val == root.val:
                right = r
            else:
                right = 0
                
            self.res = max(self.res, left + right + 1)
            return max(left, right) + 1
        
        helper(root)
        return self.res - 1  
        
 #124
 class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = -inf
        def helper(root):
            if not root:
                return 0
            
            l = helper(root.left)
            r = helper(root.right)
            
            l = 0 if l < 0 else l
            r = 0 if r < 0 else r
            
            self.res = max(self.res, l+r+root.val)
            
            return max(l, r) + root.val
        helper(root)
        return self.res
        
        
        
        
        
        
        
        
        
