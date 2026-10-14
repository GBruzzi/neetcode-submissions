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
        fast = head
        middle = fast
        antes_middle = None

        while fast and fast.next:
            fast = fast.next.next
            antes_middle = middle
            middle = middle.next

        # lista impar
        if fast:
            antes_middle = middle
            middle = middle.next

        antes_middle.next = None

        revert = middle
        prev = None

        while revert:
            tmp = revert.next
            revert.next = prev
            prev = revert
            revert = tmp

        proximo = head
        anterior = prev

        while anterior:
            next_proximo = proximo.next
            next_anterior = anterior.next

            proximo.next = anterior
            anterior.next = next_proximo

            proximo = next_proximo
            anterior = next_anterior
        

        

        