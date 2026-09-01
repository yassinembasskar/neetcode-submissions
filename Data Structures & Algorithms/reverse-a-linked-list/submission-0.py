class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        next_head = head
        head = head.next
        next_head.next = None
        while head:
            tmp = head.next
            head.next = next_head
            next_head = head
            head = tmp

        return next_head

            
             
            