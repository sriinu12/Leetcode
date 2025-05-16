from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Compute the maximum profit from one buy-sell transaction.
        Uses a single pass, O(n) time and O(1) space.
        """
        min_price = float('inf')  # lowest price we've seen so far
        max_profit = 0            # best profit we've made so far

        for price in prices:
            # If this price is lower than any we've seen, update min_price
            if price < min_price:
                min_price = price
            else:
                # Otherwise, compute profit by selling at current price
                profit = price - min_price
                # Update max_profit if this is better
                if profit > max_profit:
                    max_profit = profit

        return max_profit
