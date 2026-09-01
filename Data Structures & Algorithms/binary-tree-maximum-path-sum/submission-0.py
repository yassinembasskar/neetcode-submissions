# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxConnected(root: Optional[TreeNode], maxim:int):
            if not root:
                return maxim
            max_left = maxConnected(root.left, maxim + root.val)
            max_right = maxConnected(root.right, maxim + root.val)
            return max(max_left, max_right, maxim)
        max_left = float("-inf")
        max_right = float("-inf")
        if root.left:
            max_left = self.maxPathSum(root.left)
        if root.right:
            max_right = self.maxPathSum(root.right)
        max_conn = maxConnected(root.right, root.val) + maxConnected(root.left, root.val) - root.val
        return max(max_left, max_right, max_conn)