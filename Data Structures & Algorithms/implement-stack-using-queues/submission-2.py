from collections import deque

class MyStack:

    def __init__(self):
        self.left = deque()
        self.right = deque()
        
    def push(self, x: int) -> None:
        self.left.append(x)
        while self.right:
            self.left.append(self.right.popleft())
        temp = self.left
        self.left = self.right 
        self.right = temp
        return 

    def pop(self) -> int:
        val = self.right[0]
        self.right.popleft()
        return val

    def top(self) -> int:
        return self.right[0]
        

    def empty(self) -> bool:
        return not self.right
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()