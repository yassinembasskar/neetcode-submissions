# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def contain(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not subRoot and not root:
                return True
            elif not subRoot or not root or root.val != subRoot.val:
                return False
            else:
                return contain(root.right, subRoot.right) and contain(root.left, subRoot.left)
        if not subRoot:
            return True
        if not root:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        else:
            if contain(root, subRoot):
                return True
            else:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)