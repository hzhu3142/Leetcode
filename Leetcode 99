class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            nonlocal x, y, pre
            inorder(root.left)
            if pre and pre.val > root.val:
                y = root
                if not x:
                    x = pre
                else:
                    return
            pre = root
            inorder(root.right)
            
        x = y = pre = None
        inorder(root)
        x.val, y.val = y.val, x.val
        
        
        Method 2(stack)
        class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = x = y = None
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                tempt = stack.pop()
                if pre and pre.val > tempt.val:
                    y = tempt
                    if not x:
                        x = pre
                    else:
                        break
                pre = tempt
                cur = tempt.right
        x.val, y.val = y.val, x.val
