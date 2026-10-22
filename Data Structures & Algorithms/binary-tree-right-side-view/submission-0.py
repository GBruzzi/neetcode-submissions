# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root :
            return []
        
        res = []
        q = deque()

        q.append(root)

        while q:
            res.append(q[-1].val)
            n = len(q)
            
            for i in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        
        return res
