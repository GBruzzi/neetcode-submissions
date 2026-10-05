# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        atual = ListNode()
        res = atual

        while list1 and list2:
            if list1.val < list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next

            atual = atual.next

        atual.next = list1 or list2

        return res.next

        return res.next
