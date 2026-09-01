# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:                     
        res = []
        def expandRes(root: Optional[TreeNode], level:int):
            if root:
                if len(res) == level:
                    res.append([root.val])
                else:
                    res[level].append(root.val)
                expandRes(root.left, level+1)
                expandRes(root.right, level+1)
        
        expandRes(root, 0)
        return res
        