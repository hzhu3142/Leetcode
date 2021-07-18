class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.ranks = [1] * (n+1)
        
    def find(self, u):
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
            
        return u
    
    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return False
        elif self.ranks[parent_u] > self.ranks[parent_v]:
            self.parents[parent_v] = parent_u
        elif self.ranks[parent_u] < self.ranks[parent_v]:
            self.parents[parent_u] = parent_v
        else:
            self.parents[parent_v] = parent_u
            self.ranks[parent_u] += 1
            
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        s = UnionFindSet(len(edges))
        for edge in edges:
            if not s.union(edge[0], edge[1]):
                return edge
        
        return None
