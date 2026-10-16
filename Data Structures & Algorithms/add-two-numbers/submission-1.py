# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()

        pointer = dummy
        carry = False


        while l1 and l2:
            soma = (l1.val + l2.val + carry) % 10

            if (l1.val + l2.val + carry) > 9:
                carry = True
            else:
                carry = False

            pointer.next = ListNode(soma)

            l1 = l1.next
            l2 = l2.next
            pointer = pointer.next

        existe = l1 or l2
        while existe:
            soma = (existe.val + carry) %10

            if (existe.val + carry) > 9:
                carry = True
            else:
                carry = False

            pointer.next = ListNode(soma)
            existe = existe.next
            pointer = pointer.next

        if carry:
            pointer.next = ListNode(1)

        return dummy.next

