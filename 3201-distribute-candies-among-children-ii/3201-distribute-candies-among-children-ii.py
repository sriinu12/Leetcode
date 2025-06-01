class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb2(x: int) -> int:
            return x * (x - 1) // 2 if x >= 2 else 0

        # If n is too large, every distribution forces someone > limit
        if n > 3 * limit:
            return 0

        # 1) Count all ways to put n candies into 3 slots (bins) unconstrained:
        #    That is C(n + 2, 2).   (Imagine n candies + 2 “bars” for partitions.)
        total_ways = comb2(n + 2)

        L = limit + 1

        # 2) Subtract distributions where at least one child > limit:
        #    If one child gets ≥ L candies, we “reserve” L candies for that child,
        #    then distribute the remaining (n - L) among 3 children freely.
        #    Number of ways to distribute (n - L) among 3 kids unconstrained is C((n - L) + 2, 2),
        #    and there are 3 choices of which child is over limit.
        ways_exceed_one = 3 * comb2((n - L) + 2)

        # 3) Add back distributions where at least two children > limit (since we subtracted them twice):
        #    Reserve 2·L candies (L to child A and L to child B), 
        #    distribute (n - 2L) among 3 kids freely → C((n - 2L) + 2, 2).
        #    There are C(3, 2) = 3 ways to choose those two children.
        ways_exceed_two = 3 * comb2((n - 2 * L) + 2)

        # 4) Subtract distributions where all three children > limit (since we added them back three times):
        #    If each child has at least L, that’s 3·L reserved; distribute (n - 3L) among 3 freely.
        #    There’s exactly 1 way to pick all three as the “over-limit” set.
        ways_exceed_three = comb2((n - 3 * L) + 2)

        return total_ways - ways_exceed_one + ways_exceed_two - ways_exceed_three
        