# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        tmp = ListNode(0, head)
        before = tmp

        for _ in range(left - 1):
            before = before.next
        
        start = before.next
        curr = start
        prev = None
        
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before.next = prev
        start.next = curr
        return tmp.next