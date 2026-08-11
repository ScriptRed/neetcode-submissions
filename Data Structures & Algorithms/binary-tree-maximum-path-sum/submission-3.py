# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxFound = float("-inf")

        def dfs(node):
            if not node:
                return float("-inf")
            maxleft = dfs(node.left)
            maxright = dfs(node.right)
            self.maxFound = max(self.maxFound,node.val + maxleft + maxright,node.val,maxleft + node.val,maxright + node.val)

            return max(node.val,maxleft + node.val,maxright + node.val)
        dfs(root)
        return self.maxFound

