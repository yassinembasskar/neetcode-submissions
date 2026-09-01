# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            
            leftside = dfs(root.left)
            rightside = dfs(root.right)
            res = max(res, rightside + leftside)
            return 1 + max(leftside, rightside)

        dfs(root)
        return res