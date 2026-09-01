# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nbNodes = 0
        def maxNode(root: TreeNode, maxim: int):
            nonlocal nbNodes
            if not root:
                return 
            if root.val >= maxim:
                nbNodes += 1
            maxNode(root.left, max(maxim, root.val))
            maxNode(root.right, max(maxim, root.val))
        maxNode(root, float("-inf"))
        return nbNodes
