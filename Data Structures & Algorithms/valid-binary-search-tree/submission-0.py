# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def between(root: Optional[TreeNode], minim: int, maxim: int):
            if not root:
                return True
            if root.val > minim and root.val < maxim:
                return between(root.right, root.val, maxim) and between(root.left, minim, root.val)
            return False
        return between(root, float("-inf"), float("+inf"))