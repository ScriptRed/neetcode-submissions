# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = right = ListNode(0,head)
        groupPrev = dummy

        while right:
            for i in range(k):
                if right:
                    right = right.next

            if right:
                groupNext = right.next
                prev = groupNext
                curr = groupPrev.next

                while curr != groupNext:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                temp = groupPrev.next
                groupPrev.next = right
                groupPrev = temp
                right = groupPrev
            
            else:
                break
                
        return dummy.next
