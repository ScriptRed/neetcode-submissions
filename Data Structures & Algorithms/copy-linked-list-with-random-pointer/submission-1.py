"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newMap = {}

        curr = Node(head.val, None, None)
        newMap[head] = curr
        start = curr

        orig = head.next
        while orig:
            curr.next = Node(orig.val, None, None)
            curr = curr.next
            newMap[orig] = curr
            orig = orig.next

        orig = head
        curr = start
        while orig:
            if orig.random:
                curr.random = newMap[orig.random]
            orig = orig.next
            curr = curr.next

        return start
