class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # 1) Generate all valid column states (no adjacent equal vertically)
        states = []
        def gen(state=()):
            if len(state) == m:
                states.append(state)
                return
            for c in range(3):
                if not state or state[-1] != c:
                    gen(state + (c,))
        gen()
        
        S = len(states)
        
        # 2) Precompute compatibility: which states can follow which
        compat = [[] for _ in range(S)]
        for i, s in enumerate(states):
            for j, t in enumerate(states):
                # check horizontal compatibility: no same color in same row
                if all(s[r] != t[r] for r in range(m)):
                    compat[i].append(j)
        
        # 3) DP over columns using rolling arrays
        # dp[i] = ways to end column j in state i
        dp = [1] * S  # column 0: any valid single column
        for _col in range(1, n):
            new_dp = [0] * S
            for i in range(S):
                cnt_i = dp[i]
                if not cnt_i:
                    continue
                for j in compat[i]:
                    new_dp[j] = (new_dp[j] + cnt_i) % MOD
            dp = new_dp
        
        # 4) Sum over all end-states
        return sum(dp) % MOD
        