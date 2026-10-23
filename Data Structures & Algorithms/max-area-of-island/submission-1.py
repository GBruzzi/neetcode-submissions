class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        res = 0

        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    value = self.dfs(i,j,visited,grid)        

                    res = max(res,value)

        return res

    

    def dfs(self,linha,coluna,visited,grid):
        if linha < 0 or linha >= len(grid) or coluna < 0 or coluna >= len(grid[0]):
            return 0

        if (linha,coluna) in visited or grid[linha][coluna] == 0:
            return 0

        visited.add((linha,coluna))

        return 1 + self.dfs(linha,coluna + 1,visited,grid) + self.dfs(linha,coluna - 1,visited,grid) + self.dfs(linha - 1,coluna,visited,grid) + self.dfs(linha + 1,coluna,visited,grid)
