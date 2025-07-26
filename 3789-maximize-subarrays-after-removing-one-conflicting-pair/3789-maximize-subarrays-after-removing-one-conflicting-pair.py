class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        validSubarrays = 0
        maxLeft = 0
        secondMaxLeft = 0
        # gains[i]: extra valid subarrays if we remove the conflict at i
        gains = [0] * (n + 1)
        # conflicts[r]: list of left‐endpoints that conflict with any subarray ending at r
        conflicts = [[] for _ in range(n + 1)]

        # Build conflict lists keyed by the larger endpoint
        for a, b in conflictingPairs:
            right = max(a, b)
            left  = min(a, b)
            conflicts[right].append(left)

        # Sweep right endpoint from 1..n
        for right in range(1, n + 1):
            for left in conflicts[right]:
                # Maintain the top two largest conflicting lefts
                if left > maxLeft:
                    secondMaxLeft, maxLeft = maxLeft, left
                elif left > secondMaxLeft:
                    secondMaxLeft = left

            # Count all subarrays ending at `right` that start after maxLeft
            validSubarrays += right - maxLeft
            # If we remove the conflict at maxLeft, we gain starts from (secondMaxLeft+1) to maxLeft
            gains[maxLeft] += maxLeft - secondMaxLeft

        # Best single removal adds the largest gain
        return validSubarrays + max(gains)
        