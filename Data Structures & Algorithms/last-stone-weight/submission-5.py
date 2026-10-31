import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        if len(heap) == 1:
            return -heap[0]

        while(len(heap) > 1):
            print(heap)
            x = abs(heapq.heappop(heap))
            y = abs(heapq.heappop(heap))
            result = abs(x - y)
            if result > 0:
                heapq.heappush(heap, -result)
            
        return -heap[0] if heap else 0
