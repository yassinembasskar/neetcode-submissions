"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hash_map = {}
        stack = [node]
        while stack:
            visit_node = stack.pop()
            if visit_node.val not in hash_map:
                hash_map[visit_node.val] = Node(visit_node.val)
            for neighbor in visit_node.neighbors:
                if neighbor.val not in hash_map:
                    stack.append(neighbor)
                    tmp = Node(neighbor.val)
                    hash_map[neighbor.val] = tmp
                hash_map[visit_node.val].neighbors.append(hash_map[neighbor.val])


        return hash_map[1]
