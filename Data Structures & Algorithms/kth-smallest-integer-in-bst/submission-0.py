# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.res = []

        self.innorder(root)

        return self.res[k - 1]
    
    def innorder(self,node):
        if not node:
            return

        self.innorder(node.left)
        self.res.append(node.val)
        self.innorder(node.right)