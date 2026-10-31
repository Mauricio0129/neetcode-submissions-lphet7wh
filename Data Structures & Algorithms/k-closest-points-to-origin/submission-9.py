class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [float("-inf")]
        for point in points:
            self.add(point, heap, k)
        return heap[1:]

    def add(self, point, heap, k):
        if len(heap) <= k:
            heap.append(point) ## add to vp list 
            index = len(heap) - 1  ## adjust index

            while (index // 2 > 0):
                child_value = heap[index][0] ** 2 + heap[index][1] ** 2  ## child value
                parent_value = heap[index // 2][0] ** 2 + heap[index // 2][1] ** 2 # parent

                if child_value > parent_value:
                    temp = heap[index // 2] ## store parent
                    heap[index // 2] = heap[index]  ## update parent with child data
                    heap[index] = temp  ## update chield with parent data 

                    index = index // 2
                else:
                    break
        else:
            point_value = point[0] ** 2 + point[1] ** 2
            root_value = heap[1][0] ** 2 + heap[1][1] ** 2 

            if point_value > root_value:
                return

            else:
                heap[1] = point
                index = 1

                while(index * 2 < len(heap)):
                    if ((index * 2 + 1 < len(heap)) and 
                    ((heap[index * 2 + 1][0] ** 2 + heap[index * 2 + 1][1] ** 2) > (heap[index * 2][0] ** 2 + heap[index * 2][1] ** 2)) and
                    ((heap[index][0] ** 2 + heap[index][1] ** 2) < (heap[index * 2 + 1][0] ** 2 + heap[index * 2 + 1][1] ** 2))):
                        

                        temp = heap[index * 2 + 1]
                        heap[index * 2 + 1] = heap[index]
                        heap[index] = temp
                        index = index * 2 + 1

                    elif(heap[index][0] ** 2 + heap[index][1] ** 2) < (heap[index * 2][0] ** 2 + heap[index * 2][1] ** 2):
                        
                        temp = heap[index * 2]
                        heap[index * 2] = heap[index]
                        heap[index] = temp

                        index = index * 2
                    else:
                        break

        return 

                














        