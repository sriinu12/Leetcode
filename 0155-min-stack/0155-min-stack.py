class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        """
        Pushes x onto the stack, and updates the current minimum.
        """
        self.main_stack.append(x)
        # If min_stack is empty or x is new minimum, push x;
        # otherwise repeat the current minimum.
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        # Pop from both stacks to keep them in sync
        self.main_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        """
        Gets the top element.
        """
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()