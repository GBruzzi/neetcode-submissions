class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        d = {}

        for i in range(numCourses):
            d[i] = []

        for pair in prerequisites:
            d[pair[0]].append(pair[1])

        visited = set()
        checked = set()

        for i in range(numCourses):
            if self.dfs(i, visited, checked, d) == False:
                return False

        return True

    def dfs(self, node, visited, checked, graph):
        if node in checked:
            return True

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if not self.dfs(neighbor, visited, checked, graph):
                return False

        visited.remove(node)
        checked.add(node)

        return True