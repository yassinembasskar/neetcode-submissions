# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rightRes(root: Optional[TreeNode], level:int):
            if root:
                if len(res) == level:
                    res.append(root.val)
                else:
                    res[level] = root.val
                rightRes(root.left, level+1)
                rightRes(root.right, level+1)
        rightRes(root, 0)
        return res