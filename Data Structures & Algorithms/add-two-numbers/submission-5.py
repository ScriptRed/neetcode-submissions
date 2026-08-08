# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curl2 = l2
        curl1 = l1
        
        while l1.next or l2.next:
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            elif l2.next and not l1.next:
                l1.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next





        dummy = res = ListNode()

        l2 = curl2
        l1 = curl1

        carry = 0
        while l1 or carry > 0:
            if not l1:
                res.next = ListNode(carry)
                carry = 0
            else:
                res.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next

            res = res.next
        return dummy.next

        