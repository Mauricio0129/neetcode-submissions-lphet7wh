# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ahead, new_head = self.helper(head)
        return new_head
    
    def helper(self, head):
        if not head.next:
            return head, head
        
        ahead, new_head = self.helper(head.next) 
        ahead.next = head
        head.next = None

        return head, new_head
        