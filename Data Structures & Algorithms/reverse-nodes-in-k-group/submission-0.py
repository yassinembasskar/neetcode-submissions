# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        new_list = []
        curr = head
        while curr:
            new_list.append(curr.val)
            curr = curr.next
        
        new_head = courr = None
        j = 1
        while (j*k <= len(new_list)):
            for i in range(j*k-1, (j-1)*k-1, -1):
                if not new_head:
                    new_head = courr = ListNode(new_list[i])
                    courr.next = None
                else:
                    courr.next = ListNode(new_list[i])
                    courr = courr.next
                    courr.next = None
            j+=1

        for i in range((j-1)*k, len(new_list)):
            if not new_head:
                new_head = courr = ListNode(new_list[i])
                courr.next = None
            else:
                courr.next = ListNode(new_list[i])
                courr = courr.next
                courr.next = None
        return new_head
                
            
