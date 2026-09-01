# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def contain(root: 'TreeNode', value:int):
            if not root:
                return False
            if root.val == value: 
                return True 
            else:
                return contain(root.left, value) or contain(root.right, value)
        
        if contain(root.right, p.val) and contain(root.right, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif contain(root.left, p.val) and contain(root.left, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
