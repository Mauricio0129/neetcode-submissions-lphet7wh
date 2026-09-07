class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, i, smallest_node.next))

        return dummy_head.next