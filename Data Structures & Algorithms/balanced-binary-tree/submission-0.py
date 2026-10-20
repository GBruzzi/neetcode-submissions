# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.res = True

        self.dfs(root)

        return self.res


    def dfs(self,node):
        if not node:
            return 0

        esq = self.dfs(node.left)
        dir = self.dfs(node.right)

        if abs(esq - dir) > 1:
            self.res = False

        return 1 + max(esq,dir)