class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = [float("-inf")]
        self.target = k
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) <= self.target:
            self.heap.append(val)
            index = len(self.heap) - 1
            
            while index // 2 > 0:
                if self.heap[index] < self.heap[index // 2]:
                    self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                    index = index // 2
                else:
                    break  
        else:
            if val <= self.heap[1]:
                return self.heap[1]
            
            self.heap[1] = val
            index = 1

            while index * 2 < len(self.heap):
                left = index * 2
                right = index * 2 + 1
                
                if right < len(self.heap) and self.heap[right] < self.heap[left] and self.heap[right] < self.heap[index]:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                    index = right
                    
                elif self.heap[left] < self.heap[index]:
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                    index = left
                    
                else:
                    break 

        return self.heap[1]