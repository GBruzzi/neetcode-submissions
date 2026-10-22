# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.dfs(root,-math.inf,math.inf)

    def dfs(self,node,menor,maior):
        if not node:
            return True

        if node.val <= menor or node.val >= maior:
            return False

        return self.dfs(node.left,menor,node.val) and self.dfs(node.right,node.val,maior)

        