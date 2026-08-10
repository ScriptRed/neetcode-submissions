# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = deque([root])
        while stack:
            buffer = []
            for i in range(len(stack)):
                item = stack.popleft()
                buffer.append(item.val)
                if item.left:
                    stack.append(item.left)
                if item.right:
                    stack.append(item.right)
            res.append(buffer)
        return res