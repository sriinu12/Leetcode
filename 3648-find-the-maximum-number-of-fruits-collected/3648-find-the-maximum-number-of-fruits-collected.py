from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        # 1) Sum up child1’s forced diagonal path and zero it out
        diag_sum = 0
        for i in range(n):
            diag_sum += fruits[i][i]
            fruits[i][i] = 0
        
        # A safe “-infinity”
        NEG_INF = -10**18
        
        # 2) DP for child2 from (0, n-1) down to (n-1, n-1)
        #    allowed moves: (1,  -1), (1, 0), (1, +1)
        dp2_prev = [NEG_INF] * n
        dp2_prev[n-1] = fruits[0][n-1]
        for r in range(1, n):
            dp2_curr = [NEG_INF] * n
            for c in range(n):
                best = dp2_prev[c]
                if c > 0:
                    best = max(best, dp2_prev[c-1])
                if c+1 < n:
                    best = max(best, dp2_prev[c+1])
                if best > NEG_INF:
                    dp2_curr[c] = best + fruits[r][c]
            dp2_prev = dp2_curr
        child2_best = dp2_prev[n-1]
        
        # 3) DP for child3 from (n-1, 0) across to (n-1, n-1)
        #    allowed moves: (-1, +1), (0, +1), (+1, +1)
        dp3_prev = [NEG_INF] * n
        dp3_prev[n-1] = fruits[n-1][0]
        for c in range(1, n):
            dp3_curr = [NEG_INF] * n
            for r in range(n):
                best = dp3_prev[r]
                if r > 0:
                    best = max(best, dp3_prev[r-1])
                if r+1 < n:
                    best = max(best, dp3_prev[r+1])
                if best > NEG_INF:
                    dp3_curr[r] = best + fruits[r][c]
            dp3_prev = dp3_curr
        child3_best = dp3_prev[n-1]
        
        return diag_sum + child2_best + child3_best
