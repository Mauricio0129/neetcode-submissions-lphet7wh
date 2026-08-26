class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    class ListNode:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1 

        temp = self.head
        for i in range(index):
            temp = temp.next

        return temp.value
        

    def addAtHead(self, val: int) -> None:
        new_node = self.ListNode(val)

        if not self.head:
            self.tail = self.head = new_node
            self.length += 1
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = self.ListNode(val)

        if not self.head:
            self.tail = self.head = new_node
            self.length += 1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return

        elif index == self.length:
            return self.addAtTail(val)

        elif index == 0:
            return self.addAtHead(val)

        else:
            new_node = self.ListNode(val)
            ahead = self.head

            for i in range(index):
                ahead = ahead.next

            new_node.next = ahead
            new_node.prev = ahead.prev
            new_node.prev.next = new_node
            ahead.prev = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        
        elif self.length == 1:
            self.tail = self.head = None
            self.length -= 1
            return 
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None

        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            onpoint = self.head
            for i in range(index):
                onpoint = onpoint.next
            
            onpoint.prev.next = onpoint.next
            onpoint.next.prev = onpoint.prev

        self.length -= 1
        return


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)