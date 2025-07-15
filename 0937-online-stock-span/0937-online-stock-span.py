class StockSpanner:

    def __init__(self):
        # Stack holds pairs (price, span)
        self.stack = []
        

    def next(self, price: int) -> int:
        # Start with span = 1 (today itself)
        curr_span = 1
        
        # Merge with any consecutive days having price ≤ today's
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            curr_span += prev_span
        
        # Record today’s price with its computed span
        self.stack.append((price, curr_span))
        
        return curr_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)