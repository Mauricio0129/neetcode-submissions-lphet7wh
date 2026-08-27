class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = self.ListNode(homepage)

    class ListNode:

        def __init__(self, url):
            self.next = None
            self.prev = None
            self.url = url

    def visit(self, url: str) -> None:
        new_node = self.ListNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)