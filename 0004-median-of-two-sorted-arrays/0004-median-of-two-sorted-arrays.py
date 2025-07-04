class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        
        # Binary search on nums1’s cut position
        low, high = 0, m
        half = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2           # cut in nums1
            j = half - i                    # corresponding cut in nums2
            
            # Boundary values or “infinity” to simplify comparisons
            Aleft  = nums1[i-1] if i > 0 else float("-inf")
            Aright = nums1[i]   if i < m else float("inf")
            Bleft  = nums2[j-1] if j > 0 else float("-inf")
            Bright = nums2[j]   if j < n else float("inf")
            
            # Check if we’ve found a valid partition
            if Aleft <= Bright and Bleft <= Aright:
                # Compute median based on even/odd total length
                if (m + n) % 2:  # odd
                    return max(Aleft, Bleft)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # We’ve cut too far right in nums1; move left
                high = i - 1
            else:
                # We’ve cut too far left in nums1; move right
                low = i + 1
        
        # Control should never reach here if inputs are valid
        raise ValueError("Input arrays are not sorted or lengths invalid")
        