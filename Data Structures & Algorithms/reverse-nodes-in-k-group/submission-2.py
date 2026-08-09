# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = res = ListNode()
        buffer = [None]*k

        while head:
            for i in range(k):
                if head:
                    buffer[i] = head
                    head = head.next
            if buffer[-1]:
                for i in range(k-1,-1,-1):
                    res.next = buffer[i]
                    res = res.next
                res.next = None
                buffer = [None]*k
            else:
                for i in range(k):
                    res.next = buffer[i]
                    if not buffer[i+1]:
                        break
                    res = res.next
        return dummy.next
