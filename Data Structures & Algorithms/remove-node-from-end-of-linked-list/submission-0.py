# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next:
            return None

        count = 0

        pointer = head

        while pointer:
            pointer = pointer.next
            count += 1

        remove = head

        if (count - n - 1) < 0:
            tmp = head.next
            head.next = None
            head = tmp
            return head

        while count - n - 1:
            remove = remove.next
            count -= 1
 

        if remove.next and remove.next.next:
            remove.next = remove.next.next
        elif remove.next:
            remove.next = None

        return head