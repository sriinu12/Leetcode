class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[i][j]: longest valid subseq ending with residues (i, j)
        dp = [[0] * k for _ in range(k)]
        ans = 0

        for num in nums:
            r = num % k
            # update dp for appending this number
            for i in range(k):
                dp[i][r] = dp[r][i] + 1
                if dp[i][r] > ans:
                    ans = dp[i][r]

        return ans
        