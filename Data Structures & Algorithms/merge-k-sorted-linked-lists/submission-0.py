# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_list = []
        for l in lists:
            while l:
                new_list.append(l.val)
                l = l.next
        
        new_head = courr = None

        for n in sorted(new_list):
            if not new_head:
                new_head = courr = ListNode()
            else:
                courr.next = ListNode()
                courr = courr.next
            courr.val = n
            courr.next = None

        return new_head
            