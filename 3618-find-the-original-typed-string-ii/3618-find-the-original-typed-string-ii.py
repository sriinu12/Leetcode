class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)
        
        # 1) Run-length encode
        groups = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        
        m = len(groups)
        
        # 2) Total combinations = ∏ g_i
        total = 1
        for g in groups:
            total = (total * g) % MOD
        
        # 3) If minimal possible length (one per group) ≥ k, we're done
        if m >= k:
            return total
        
        # 4) DP to count how many pick‐choices give total length < k
        # dp[j] = number of ways to pick from runs seen so far so that sum = j
        dp = [0] * k
        dp[0] = 1
        
        for g in groups:
            new_dp = [0] * k
            window = 0
            # We want new_dp[j] = sum(dp[j-1], dp[j-2], …, dp[j-g])
            # which we can maintain as a sliding window over dp
            for j in range(k):
                # add dp[j-1] into window
                if j - 1 >= 0:
                    window = (window + dp[j - 1]) % MOD
                # remove dp[j-g-1] once the window exceeds size g
                if j - g - 1 >= 0:
                    window = (window - dp[j - g - 1] + MOD) % MOD
                new_dp[j] = window
            dp = new_dp
        
        short_count = sum(dp) % MOD
        
        # 5) Answer = total – (# too‐short combinations)
        return (total - short_count + MOD) % MOD
        