from typing import List

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        """
        Returns the count of distinct bitwise-ORs of all contiguous subarrays of A.
        Uses a rolling set of OR-results ending at the previous index to
        build results for the current index in O(B) time per element (B = bit-width).
        """
        ans = set()         # all distinct OR-results seen so far
        prev_set = set()    # OR-results of subarrays ending at A[i-1]
        
        for x in A:
            # Start fresh subarray at x, then extend all previous
            curr_set = {x}
            for v in prev_set:
                curr_set.add(v | x)
            
            # Add all new OR-values to the global answer
            ans |= curr_set
            
            # Slide window: current becomes previous for next iteration
            prev_set = curr_set
        
        return len(ans)
