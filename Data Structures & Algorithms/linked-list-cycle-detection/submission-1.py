# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = head
        i = 10
        while curr:
            fast = fast.next
            if not fast:
                return False
            if curr == fast:
                return True
            i+=1
            if i > 2:
                i = 0
                curr = curr.next
        return False