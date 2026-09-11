class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.helper(points, 0, len(points) - 1, k - 1)

    def helper(self, points, s, e, k):

        next_smallest = s
        pivot_value = points[e][0] ** 2 + points[e][1] ** 2

        for i in range(s, e):
            current_value = points[i][0] ** 2 + points[i][1] ** 2

            if current_value < pivot_value:
                points[next_smallest], points[i] = points[i], points[next_smallest]
                next_smallest += 1
        
        points[next_smallest], points[e] = points[e], points[next_smallest]

        if next_smallest == k:
            return points[:k+1]
        elif next_smallest < k:
            return self.helper(points, next_smallest + 1, e, k)
        else:
            return self.helper(points, s, next_smallest - 1, k)









        