# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            head = None
            return head
        
        i = 0
        curr = head
        while curr:
            i+=1
            curr = curr.next
        
        if n == i:
            head = head.next
            return head
        
        i = i-n
        curr = head
        while curr and i>1:
            curr = curr.next
            i-=1
        
        curr.next = curr.next.next
        return head

