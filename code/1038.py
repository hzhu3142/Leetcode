# recursion
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.curSum = 0
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.right)
            self.curSum += root.val
            root.val = self.curSum
            inorder(root.left)
            
        inorder(root)
        return root
        
# iteration        
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        cur = root
        curSum = 0
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                curSum += cur.val
                cur.val = curSum
                cur = cur.left
        return root
