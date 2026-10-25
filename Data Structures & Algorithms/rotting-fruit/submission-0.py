class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        visited = set()
        q = deque()

        cFrescas = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    cFrescas += 1

        if not cFrescas:
            return 0

        count = -1

        while q:
            for i in range(len(q)):
                l,c = q.popleft()
                grid[l][c] = 2

                self.addNode(l + 1,c,visited,grid,q)
                self.addNode(l - 1,c,visited,grid,q)
                self.addNode(l,c + 1,visited,grid,q)
                self.addNode(l,c - 1,visited,grid,q)

            count += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]) == 1:
                    return -1

        return count


    def addNode(self,l,c,visited,grid,q):
        if (l,c) in visited or l < 0 or c < 0 or l > len(grid) - 1 or c > len(grid[l]) - 1 or grid[l][c] == 0:
            return

        q.append((l,c))
        visited.add((l,c))



    