from typing import List

MOD = 1_000_000_007

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Collect exponents of set bits (ascending by position)
        exps = []
        pos = 0
        x = n
        while x:
            if x & 1:
                exps.append(pos)
            x >>= 1
            pos += 1

        # Prefix sums of exponents
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        # Answer queries: product = 2^(sum of exponents in [l..r]) mod MOD
        ans = []
        for l, r in queries:
            s = pref[r + 1] - pref[l]
            ans.append(pow(2, s, MOD))
        return ans
