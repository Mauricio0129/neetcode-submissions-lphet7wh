import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest_solution = None
        l, r = 1, max(piles)

        while l <= r:
            middle = (r + l) // 2
            hours_count = 0

            for pile in piles:
                hours_count += math.ceil(pile / middle)
            
            if hours_count <= h:
                smallest_solution = middle
                r = middle - 1

            else:
                l = middle + 1

        return smallest_solution
        



