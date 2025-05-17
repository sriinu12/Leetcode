from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int,
                    nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place, producing a single sorted array.
        Uses the two-pointer approach, filling from the back.
        Time: O(m+n), Space: O(1).
        """
        i, j, write = m - 1, n - 1, m + n - 1

        # Merge the two arrays starting from their ends
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1

        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[write] = nums2[j]
            j -= 1
            write -= 1
        # nums1’s remaining elements (if any) are already in place
