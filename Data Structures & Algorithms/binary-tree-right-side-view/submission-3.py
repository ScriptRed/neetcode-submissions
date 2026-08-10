# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            right = queue.pop()
            res.append(right.val)
            queue.append(right)

            for i in range(len(queue)):
                item = queue.popleft()
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
        return res
