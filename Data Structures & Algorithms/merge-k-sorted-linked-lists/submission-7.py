class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        nothing_counter = 0
        length = len(lists)
        for val in lists:
            if not val:
                nothing_counter += 1
        if nothing_counter == length:
            return None
        return  self.helper(lists, 0, length -1)
    

    def helper(self, lists, s, e):
        if e - s + 1 <= 1:
            return lists[s]
        
        middle = (e + s) // 2

        return self.merge(self.helper(lists, s, middle), self.helper(lists, middle + 1, e))

    def merge(self, list1, list2):
        head = ListNode()

        runner = head
        while list1 and list2:
            if list1.val <= list2.val:
                runner.next = list1
                list1 = list1.next
            else:
                runner.next = list2
                list2 = list2.next
            runner = runner.next
        
        runner.next = list1 or list2

        return head.next

