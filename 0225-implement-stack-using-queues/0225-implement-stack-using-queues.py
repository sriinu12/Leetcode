class MyStack:

    def __init__(self):
        # We'll use a single deque as our queue
        self.q = deque()
        

    def push(self, x: int) -> None:
         # 1) Enqueue x
        self.q.append(x)
        # 2) Rotate the previous elements behind x
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        # Dequeue from front → top of stack
        return self.q.popleft()
        

    def top(self) -> int:
        # Peek at front without removing
        return self.q[0]
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()