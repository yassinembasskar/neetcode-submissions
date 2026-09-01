# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(res)
        return ",".join(res)

            
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = iter(data.split(','))
        def dfs():
            val = next(res)
            if val == "N":
                return None
            mid = TreeNode(int(val))
            mid.left = dfs()
            mid.right = dfs()
            return mid

        return dfs()