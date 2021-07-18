# single parent
# one root -> connected

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = set(range(n))
        for i in range(len(leftChild)):
            if leftChild[i] != -1:
                if leftChild[i] in root:
                    root.remove(leftChild[i])
                else:
                    return False
            
            if rightChild[i] != -1:
                if rightChild[i] in root:
                    root.remove(rightChild[i])
                else:
                    return False
        
        if len(root) != 1:
            return False
        
        visited = set()
        root = list(root)[0]
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if node in visited:
                return False
            
            visited.add(node)
            
            if leftChild[node] != -1:
                queue.append(leftChild[node])
                
                
            if rightChild[node] != -1:
                queue.append(rightChild[node])
        
    
        return len(visited) == n
