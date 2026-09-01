"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dictionnary = {}

        while curr:
            dictionnary[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                dictionnary[curr].next = dictionnary[curr.next]
            else:
                dictionnary[curr].next = None
            if curr.random:
                dictionnary[curr].random = dictionnary[curr.random]
            else:
                dictionnary[curr].random = None

            curr = curr.next
            
        if head:
            return dictionnary[head]
        return None