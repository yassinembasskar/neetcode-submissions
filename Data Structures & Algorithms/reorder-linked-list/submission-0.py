# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        liste = []
        curr = head

        while curr:
            liste.append(curr.val)
            curr = curr.next
        
        right = len(liste)-1
        left = 0
        curr = head
        while right > left:
            curr.val = liste[left]
            curr = curr.next
            curr.val = liste[right]
            curr = curr.next
            left += 1
            right -= 1

        if right == left:
            curr.val = liste[right]


        