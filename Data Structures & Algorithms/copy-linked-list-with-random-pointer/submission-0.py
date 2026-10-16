"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d = {}

        point = head

        while point:
            new_node = Node(point.val)
            d[point] = new_node

            point = point.next


        new_node = d[head]

        if not head.random:
            new_node.random = None
        else:
            new_node.random = d[head.random]

        if not head.next:
            return new_node

        new_node.next = d[head.next]
        
        res = new_node
        head = head.next
        new_node = new_node.next

        while head:
            if head.next:
                new_node.next = d[head.next]
            else:
                new_node.next = None
            

            if not head.random:
                new_node.random = None
            else:
                new_node.random = d[head.random]

            head = head.next
            new_node = new_node.next


        return res


