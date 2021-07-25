# Method 1 recursion
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


# Method 2(stack)
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        prev = None
        swap1 = swap2 = None
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev and prev.val > cur.val:
                if not swap1:
                    swap1 = prev
                    swap2 = cur
                else:
                    swap2 = cur
                    break

            prev = cur
            cur = cur.right

        swap1.val, swap2.val = swap2.val, swap1.val
        return root
