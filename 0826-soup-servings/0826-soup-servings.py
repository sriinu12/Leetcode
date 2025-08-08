class Solution:
    def soupServings(self, n: int) -> float:
        # Normalize into 25ml units
        N = ceil(n / 25)
        # For large N, probability → 1
        if N > 200:
            return 1.0

        @lru_cache(None)
        def P(i: int, j: int) -> float:
            # Base cases
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            # Recursive case: average over the 4 operations
            return 0.25 * (
                P(i - 4, j) +
                P(i - 3, j - 1) +
                P(i - 2, j - 2) +
                P(i - 1, j - 3)
            )

        return P(N, N)
        