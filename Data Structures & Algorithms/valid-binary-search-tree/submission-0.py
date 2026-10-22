# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        self.res = []      

        self.inorder(root)

        for i in range(len(self.res)- 1):
            if self.res[i + 1] <= self.res[i]:
                return False

        return True

    def inorder(self,node):
        if not node:
            return

        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)

        