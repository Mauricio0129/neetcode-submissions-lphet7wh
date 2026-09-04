class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = self.ListNode(homepage)
        self.runner = self.history
    
    class ListNode:

        def __init__(self, url, prev = None, next = None):
            self.url = url
            self.prev = prev
            self.next = next
        
    def visit(self, url: str) -> None:
        new_node = self.ListNode(url)
        self.runner.next = new_node
        new_node.prev = self.runner
        self.runner = self.runner.next    

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.runner.prev:
                self.runner = self.runner.prev
        return self.runner.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.runner.next:
                self.runner = self.runner.next
        return self.runner.url
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)