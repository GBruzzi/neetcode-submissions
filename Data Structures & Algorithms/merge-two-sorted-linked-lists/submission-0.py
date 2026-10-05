# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        atual = ListNode()
        res = atual

        while list1 or list2:
            if not list1:
                atual.next = list2
                list2 = list2.next
                atual = atual.next
            elif not list2:
                atual.next = list1
                list1 = list1.next
                atual = atual.next
            else:
                if list1.val < list2.val:
                    atual.next = list1
                    list1 = list1.next
                    atual = atual.next
                else:
                    atual.next = list2
                    list2 = list2.next
                    atual = atual.next

        return res.next
