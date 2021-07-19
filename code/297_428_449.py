#297
# In the method of dfs_ser, the res is a local variable, so in the dfs_ser, return res. If it is self.res, no need to return self.res for the dfs method.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs_ser(root):
            if not root:
                res.append('None')
                return
            res.append(str(root.val))
            dfs_ser(root.left)
            dfs_ser(root.right)
            return res
        res = []
        dfs_ser(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs_deser(q):
            if q[0] == 'None':
                q.popleft()
                return
            root = TreeNode(q.popleft())
            root.left = dfs_deser(q)
            root.right = dfs_deser(q)
            return root

        q = collections.deque(data.split(','))
        return dfs_deser(q)



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs_ser(root):
            if not root:
                self.res.append('None')
                return
            self.res.append(str(root.val))
            dfs_ser(root.left)
            dfs_ser(root.right)

        self.res = []
        dfs_ser(root)
        return ','.join(self.res)

			def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs_deser(q):
            if q[0] == 'None':
                q.popleft()
                return
            root = TreeNode(q.popleft())
            root.left = dfs_deser(q)
            root.right = dfs_deser(q)
            return root

        q = collections.deque(data.split(','))
        return dfs_deser(q)

Approach3: queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        queue = deque([root])
        while queue:
            node = queue.popleft()
            res += str(node.val) + ',' if node else 'None,'
            if node:
                queue += [node.left, node.right]
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        data = deque(data)
        root = TreeNode(int(data.popleft()))
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                left = data.popleft()
                right = data.popleft()
                cur.left = TreeNode(int(left)) if left != 'None' else None
                cur.right = TreeNode(int(right)) if right != 'None' else None
                queue += [cur.left, cur.right]

        return root


#428
class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            temp = [str(node.val), '{']
            for child in node.children:
                temp.append(str(child.val))
                queue.append(child)
            temp.append('}')
            res += ','+','.join(temp)
        return res[1:]

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        arr = data.split(',')
        root = Node(int(arr[0]), [])
        queue = deque([root])
        cur = None
        for i, ch in enumerate(arr):
            if not cur and ch.isdigit():
                cur = queue.popleft()
            elif ch == '{':
                continue
            elif ch.isdigit():
                tmp = Node(int(ch), [])
                cur.children.append(tmp)
                queue.append(tmp)
            elif ch == '}':
                cur = None
                curVal = inf

        return root


#449
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        res = ''
        cur = root
        stack = []
        while cur or stack:
            if cur:
                res += str(cur.val) + ','
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                cur = node.right
        return res[:-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(',')
        cur = root = TreeNode(int(data[0]))
        stack = []
        for num in data[1:]:
            node = TreeNode(int(num))
            if cur.val > node.val:
                cur.left = node
                stack.append(cur) # only append on stack here

            else:
                while stack and stack[-1].val < node.val:
                    cur = stack.pop()
                cur.right = node
            cur = node
        return root
