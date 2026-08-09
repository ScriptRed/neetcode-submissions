# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxDiameter = 0
        def dfs(root):
            if not root:
                return 0
            leftheight = dfs(root.left)
            rightheight = dfs(root.right)
            self.maxDiameter = max(self.maxDiameter, leftheight + rightheight)
            return max(leftheight, rightheight) + 1

        dfs(root)
        return self.maxDiameter