class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Trivial shortcuts
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        windowSum = 1.0  # sum of dp[j] with j in [i-maxPts, i-1] and j < k
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts
            if i < k:
                # This state can still draw further; keep it in the window
                windowSum += dp[i]
            else:
                # Stopping states contribute directly to the answer
                ans += dp[i]

            # Slide window: drop dp[i - maxPts] if it was included and < k
            if i - maxPts >= 0 and i - maxPts < k:
                windowSum -= dp[i - maxPts]

        return ans
        