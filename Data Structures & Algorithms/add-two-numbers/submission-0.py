# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reserved = 0
        head = ListNode()
        curr = head
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 and curr_l2:
            total_val = (curr_l1.val + curr_l2.val) + reserved
            reserved = total_val // 10
            curr.val = total_val % 10
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            if curr_l2 or curr_l1:
                curr.next = ListNode()
                curr = curr.next
        
        while curr_l1:
            total_val = curr_l1.val + reserved
            reserved = total_val // 10
            curr.val = total_val % 10
            curr_l1 = curr_l1.next
            if curr_l1:
                curr.next = ListNode()
                curr = curr.next

        while curr_l2:
            total_val = curr_l2.val + reserved
            reserved = total_val // 10
            curr.val = total_val % 10
            curr_l2 = curr_l2.next
            if curr_l2:
                curr.next = ListNode()
                curr = curr.next

        if reserved:
            curr.next = ListNode()
            curr = curr.next
            curr.val = reserved
            curr.next = None

        return head