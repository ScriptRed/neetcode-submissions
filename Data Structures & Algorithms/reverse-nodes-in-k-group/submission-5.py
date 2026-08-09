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
                else:
                    buffer[i] = None
            if buffer[-1]:
                for i in range(k - 1, -1, -1):
                    res.next = buffer[i]
                    res = res.next
            else:
                for node in buffer:
                    if not node:
                        break
                    res.next = node
                    res = res.next
        res.next = None   # single terminator
        return dummy.next
