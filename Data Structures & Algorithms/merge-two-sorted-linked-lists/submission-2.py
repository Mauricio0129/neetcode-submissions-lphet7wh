# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(-1)
        h3 = d
        
        if not list1 or not list2:
            return list2 if not list1 else list1
        
        while list1 and list2:

            if list1.val == list2.val:
                h3.next = list1
                list1 = list1.next
                h3 = h3.next
                h3.next = list2
                list2 = list2.next
                h3 = h3.next
            
            elif list1.val < list2.val:
                h3.next = list1
                list1 = list1.next
                h3 = h3.next
            
            else:
                h3.next = list2
                list2 = list2.next
                h3 = h3.next
        
        if list1 or list2:
            h3.next = list2 if not list1 else list1
        
        return d.next





