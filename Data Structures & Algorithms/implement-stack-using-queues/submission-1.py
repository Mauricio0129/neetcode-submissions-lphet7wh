from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if not self.queue1:
            self.queue1.append(x)
            self.queue1.extend(self.queue2)
            self.queue2.clear()
        else:
            self.queue2.append(x)
            self.queue2.extend(self.queue1)
            self.queue1.clear()


    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        else:
            return self.queue2.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()