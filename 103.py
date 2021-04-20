# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        #1. corner case: not root, return []
        #2. create 1) a indicator jumping between 1 and 0, if indicator = 1, left->right.
                 # 2) a temp = [0] * length, to update accordingly
                 # 3) ans, that would be my return. ans.add(temp) in every level.
                 # 4) a queue, to traverse the tree in every level
        
        if not root:
            return []
        
        indic = 1
        ans = []
        queue = deque([root])
        while queue:
            length = len(queue)
            temp = [0] * length
            for i in range(length):
                curr = queue.popleft()
                if indic:
                    temp[i] = curr.val
                else:
                    temp[length - i - 1] = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            indic = (indic + 1) % 2 # this is a cool part to change the indicator back and forth.
            ans.append(temp)
        return ans
