class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [float("-inf")]
        self.target = k
        
        for num in nums:
            if isinstance(num, int):
                self.add(num)


    def add(self, val: int) -> int:
        if len(self.heap) <= self.target:
            self.heap.append(val)
            index = len(self.heap) - 1
            while (index // 2 > 0):
                if self.heap[index] < self.heap[index // 2]:
                    temp = self.heap[index // 2]
                    self.heap[index // 2] = self.heap[index]
                    self.heap[index] = temp
                    index = index // 2
                else:
                    return self.heap[1] 
        else:
            print(self.heap,  "val",  val)
            if val <= self.heap[1]:
              
                return self.heap[1]
            
            self.heap[1] = val
            index = 1

            while (index * 2 < len(self.heap)):
                if((index * 2 + 1 < len(self.heap)) 
                and (self.heap[index * 2 + 1] < self.heap[index * 2]) 
                and (self.heap[index * 2 + 1] < self.heap[index])):

                    temp = self.heap[index]
                    self.heap[index] = self.heap[index * 2 + 1]
                    self.heap[index * 2 + 1] = temp

                    index = index * 2 + 1

                elif self.heap[index * 2] <self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[index * 2]
                    self.heap[index * 2] = temp

                    index = index * 2
                else:
                    break
            print(self.heap[1])
        return self.heap[1]
                



                

        
