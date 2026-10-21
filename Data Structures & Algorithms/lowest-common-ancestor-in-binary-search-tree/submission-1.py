# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            tmp = q
            q = p
            p = tmp

        return self.search(root,p,q)

    def search(self,root,p,q):
        if p.val < root.val and q.val > root.val:
            return root
    
        if p.val == root.val:
            return p

        if q.val == root.val:
            return q

        if p.val > root.val:
            return self.search(root.right,p,q)
        else:
            return self.search(root.left,p,q)


    



    
