# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = head

        while head and head.next:
            head = head.next.next

            if head == prev:
                return True

            prev = prev.next
        
        return False