class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == '1':
                    if (i,j) in visited:
                        continue
                    self.dfs(grid[i][j],grid,i,j,visited)
                    res += 1

        return res

    def dfs(self,node,matriz,i,j,visited):
        if node == '0':
            return

        if (i,j) in visited:
            return

        visited.add((i,j))

        if j < len(matriz[i]) - 1:
            self.dfs(matriz[i][j + 1], matriz,i,j + 1,visited)

        if i < len(matriz) - 1:
            self.dfs(matriz[i + 1][j], matriz,i + 1,j,visited)

        if j > 0:
            self.dfs(matriz[i][j - 1], matriz,i,j - 1,visited)
        
        if i > 0:
            self.dfs(matriz[i - 1][j], matriz,i - 1,j,visited)
        