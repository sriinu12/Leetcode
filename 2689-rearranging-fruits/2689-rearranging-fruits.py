class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # 1. Compute net imbalance of each fruit cost
        cnt = Counter(basket1)
        cnt.subtract(basket2)
        
        # 2. Collect half of the total excess fruits
        excess = []
        for cost, diff in cnt.items():
            # If any diff is odd, impossible to balance
            if diff % 2 != 0:
                return -1
            # Only abs(diff)//2 fruits of this cost need moving
            excess.extend([cost] * (abs(diff) // 2))
        
        # If no excess, baskets already match
        if not excess:
            return 0
        
        # 3. Sort to pair cheapest moves first
        excess.sort()
        
        # 4. The cheapest fruit overall (for potential two-swap via this fruit)
        min_cost = min(min(basket1), min(basket2))
        
        # We only need to pay for half of 'excess' entries,
        # since each swap fixes two fruits.
        half = len(excess) // 2
        
        # 5. Sum the optimal cost for each required swap
        total = 0
        for i in range(half):
            # Either swap directly (cost = excess[i])
            # or route through two cheap swaps via min_cost (cost = 2 * min_cost)
            total += min(excess[i], 2 * min_cost)
        
        return total
        