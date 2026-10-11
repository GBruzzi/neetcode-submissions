class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}

        for pair in edges:
            if pair[0] in d:
                d[pair[0]].append(pair[1])

            if pair[1] in d:
                d[pair[1]].append(pair[0])

            if pair[0] not in d:
                d[pair[0]] = [pair[1]]

            if pair[1] not in d:
                d[pair[1]] = [pair[0]]

        for i in range(n):
            if i not in d:
                d[i] = []        

        res = 0
        foi = set()

        for i in range(n):
            vis = set()
        
            if i in foi:
                continue
            
            self.dfs(d,i,vis,foi)
            res += 1

        return res




    def dfs(self,graph,node,visited,foi):
        visited.add(node)
        foi.add(node)

        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            self.dfs(graph,neighbor,visited,foi) 













