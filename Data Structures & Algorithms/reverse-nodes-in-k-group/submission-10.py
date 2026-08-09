# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = kth = ListNode(0,head)
        groupPrev = dummy

        while True:
            for i in range(k):
                if kth:
                    kth = kth.next

            if kth:
                groupNext = kth.next

                prev, curr = kth.next, groupPrev.next
                while curr != groupNext:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp

                tmp = groupPrev.next
                groupPrev.next = kth
                groupPrev = tmp
                kth = groupPrev
            else:
                break
                
        return dummy.next
