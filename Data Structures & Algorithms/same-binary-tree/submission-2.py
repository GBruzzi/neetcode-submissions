# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        res = True

        res = self.innorderTransv(p,q)

        return res

    def innorderTransv(self,node1, node2):
        if not node1 and node2 or not node2 and node1:
            return False

        if not node1 and not node2:
            return True

        if node1.val != node2.val:
            return False

        return self.innorderTransv(node1.left, node2.left) and self.innorderTransv(node1.right, node2.right)
        

        
            

