class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        # iterate over rows (skip the first row since it's all 1's)
        for _ in range(1, m):
            # update dp for each column from left to right
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        # the bottom-right corner is dp[n-1]
        return dp[-1]
        