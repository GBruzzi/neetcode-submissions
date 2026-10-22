# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        maior = root.val

        self.dfs(root,maior)

        return self.res

    def dfs(self,node,maior):
        if not node:
            return

        if node.val >= maior:
            self.res += 1
            maior = node.val

        self.dfs(node.left,maior)
        self.dfs(node.right,maior)