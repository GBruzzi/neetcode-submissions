# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        self.res = False

        if not root and not subRoot:
            return True

        self.dfs(root,subRoot)

        return self.res
    
    def sameTree(self,p,q):
        if not q and not p:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

    def dfs(self,node1,node2):
        if not node1:
            return False

        if node1.val == node2.val:
            self.res = self.sameTree(node1,node2)

        if self.res:
            return True

        if self.dfs(node1.left,node2) or self.dfs(node1.right,node2):
            return True
        