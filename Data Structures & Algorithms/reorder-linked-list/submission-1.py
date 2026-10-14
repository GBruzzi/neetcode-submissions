# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        reverse = slow.next
        slow.next = None
        prev = None

        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp

        proximo = head
        anterior = prev

        while anterior:
            proximo = head.next
            anterior = prev.next

            head.next = prev
            prev.next = proximo

            head = proximo
            prev = anterior
            