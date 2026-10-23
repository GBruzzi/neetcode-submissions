class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}

        for i in range(n):
            d[i] = []

        for pair in edges:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])

        visited = set()

        res = 0

        for i in range(n):
            if i in visited:
                continue

            self.dfs(i,d,visited)
    
            res += 1

        return res



    def dfs(self,node,graph,visited):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor in visited:
                continue
                
            self.dfs(neighbor,graph,visited)
            








