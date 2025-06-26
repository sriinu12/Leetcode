class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        num = 0        # current value of chosen subsequence
        oneCount = 0   # how many '1's we've included
        pow2 = 1       # weight of next bit (1<<0, 1<<1, ...)

        # 1) Greedily take '1's from least significant bit upwards
        for ch in reversed(s):
            if ch == '1':
                # can we include this '1'?
                if num + pow2 <= k:
                    num += pow2
                    oneCount += 1
            # update weight for next bit
            pow2 <<= 1

        # 2) Every '0' can also be used without changing value
        zeroCount = s.count('0')

        return zeroCount + oneCount
        