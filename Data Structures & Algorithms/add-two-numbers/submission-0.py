# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        new_node = ListNode()
        res = new_node

        if l1.val + l2.val > 9:
            carry = True
        else:
            carry = False

        new_node.val = (l1.val + l2.val) % 10 

        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            new_node.next = ListNode((l1.val + l2.val + carry) % 10)

            if (l1.val + l2.val + carry)  > 9 : 
                carry = True
            else :
                carry = False
            
            new_node = new_node.next
            l1 = l1.next
            l2 = l2.next

        existe = l1 or l2
        
        while existe:
            new_node.next = ListNode((existe.val + carry) % 10) 

            if (existe.val + carry)  > 9 : 
                carry = True
            else :
                carry = False

            new_node = new_node.next
            existe = existe.next

        if carry:
            new_node.next = ListNode(1)

        return res

