# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(-1)
        d.next = head

        while head and head.next:
            temp = d.next
            d.next = head.next
            head.next = head.next.next
            d.next.next = temp
        return d.next

