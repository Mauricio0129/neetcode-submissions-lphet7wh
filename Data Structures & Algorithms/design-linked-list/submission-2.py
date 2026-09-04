class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    class ListNode:
        def __init__(self, val=0, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        runner = self.head
        for _ in range(index):
            runner = runner.next
        return runner.val

    def addAtHead(self, val: int) -> None:
        new_node = self.ListNode(val)
        self.length += 1

        if not self.head:
            self.tail = self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = self.ListNode(val)
        self.length += 1
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        elif index == 0:
            return self.addAtHead(val)
        elif index == self.length:
            return self.addAtTail(val)
        else:
            new_node = self.ListNode(val)
            runner = self.head

            for _ in range(index):
                runner = runner.next
            new_node.next = runner
            new_node.prev = runner.prev

            runner.prev.next = new_node
            runner.prev = new_node
        self.length += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        elif index == 0 and self.length == 1:
            self.tail = self.head = self.head.next

        else:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif index == self.length - 1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                runner = self.head
                for _ in range(index):
                    runner = runner.next
                runner.prev.next = runner.next
                runner.next.prev = runner.prev
        self.length -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
