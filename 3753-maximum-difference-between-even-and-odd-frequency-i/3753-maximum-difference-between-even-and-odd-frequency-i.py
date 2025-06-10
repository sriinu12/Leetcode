class Solution:
    def maxDifference(self, s: str) -> int:
        freq = collections.Counter(s)
        max_odd = 0
        min_even = float('inf')
        
        for v in freq.values():
            if v % 2 == 1:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        
        # It's guaranteed there's at least one of each
        return max_odd - min_even
        