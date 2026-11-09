from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        for key, value in count.items():
            if len(res) < k:
                heapq.heappush(res, (value, key))
            else:
                heapq.heappushpop(res, (value, key))
        return [val[1] for val in res]