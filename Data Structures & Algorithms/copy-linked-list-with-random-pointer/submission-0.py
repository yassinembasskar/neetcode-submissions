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
        new_head = None
        if head:
            new_head = Node(head.val)
            new_curr = new_head
        dictionnary = {}

        while curr:
            dictionnary[curr] = new_curr
            if curr.next:
                new_curr.next = Node(curr.next.val)
                new_curr = new_curr.next
            else:
                new_curr.next = None
            curr = curr.next
        
        curr = head
        new_curr = new_head
        while curr:
            if curr.random:
                new_curr.random = dictionnary[curr.random]
            else:
                new_curr.random = None

            curr = curr.next
            new_curr = new_curr.next
        
        return new_head
