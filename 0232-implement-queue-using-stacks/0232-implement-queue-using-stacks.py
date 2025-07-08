class MyQueue:

    def __init__(self):
        # in_stack holds newly pushed items
        # out_stack holds items ready for pop/peek
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        # Always push onto in_stack
        self.in_stack.append(x)
        

    def pop(self) -> int:
        # Ensure out_stack has the current front on top
        if not self.out_stack:
            # Move all from in_stack to out_stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
        

    def peek(self) -> int:
        # Similar to pop, but without removing
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.in_stack and not self.out_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()