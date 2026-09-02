# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode()
        dummy_head.next = head

        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = dummy_head.next
            dummy_head.next = temp
        
        return dummy_head.next
