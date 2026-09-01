# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(root: Optional[TreeNode]):
            if not root:
                return 0
            return 1 + max(maxHeight(root.left), maxHeight(root.right))

        if not root:
            return True
        if -1 <= maxHeight(root.left) - maxHeight(root.right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False