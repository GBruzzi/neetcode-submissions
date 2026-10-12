class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == 1:
                    if (i,j) in visited:
                        continue
                    tamanho = []
                    self.dfs(grid[i][j],grid,i,j,visited,tamanho)
                    res = max(res, len(tamanho))  
                    
        return res

    
    def dfs(self,node,matriz,i,j,visited,tamanho):
        if node == 0:
            return

        if (i,j) in visited:
            return

        visited.add((i,j))
        tamanho.append(1)

        if j < len(matriz[i]) - 1:
            self.dfs(matriz[i][j + 1], matriz,i,j + 1,visited,tamanho)

        if i < len(matriz) - 1:
            self.dfs(matriz[i + 1][j], matriz,i + 1,j,visited,tamanho)

        if j > 0:
            self.dfs(matriz[i][j - 1], matriz,i,j - 1,visited,tamanho)
        
        if i > 0:
            self.dfs(matriz[i - 1][j], matriz,i - 1,j,visited,tamanho)

