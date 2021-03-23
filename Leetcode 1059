class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        visited = defaultdict(int)
        
        def dfs(node):
            
            if visited[node] == 1:
                return True
            
            elif visited[node] == -1:
                return False
            
            elif not graph[node]:
                return node == destination
            
            else:
                visited[node] = -1
                for nextNode in graph[node]:
                    if not dfs(nextNode):
                        return False
                visited[node] = 1
                return True
        
        return dfs(source)
        
Approach 2:

class Solution:
  
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        visited = set()
        
        def dfs(node):
            
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode == node or nextNode in visited or not dfs(nextNode):
                    return False
            visited.remove(node)
            
            # if not graph[node]:
            #     return node == destination
            # else:
            #     return node != destination
            return len(graph[node]) != 0 or node == destination
            
        
        return dfs(source)
