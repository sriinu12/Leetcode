import bisect
from typing import List

class Solution:
    def kthSmallestProduct(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> int:
        n1, n2 = len(nums1), len(nums2)
        # both arrays must be sorted ascending
        nums1.sort()
        nums2.sort()

        def count_le(x: int) -> int:
            """
            Count of pairs (i,j) with nums1[i] * nums2[j] <= x.
            """
            cnt = 0
            for a in nums1:
                if a > 0:
                    # need b <= floor(x / a)
                    t = x // a
                    cnt += bisect.bisect_right(nums2, t)
                elif a == 0:
                    # 0 * anything = 0
                    if x >= 0:
                        cnt += n2
                else:  # a < 0
                    # need b >= ceil(x / a)
                    # for a<0, ceil(x/a) = -floor(x/(-a)) = - (x // -a)
                    t = - (x // (-a))
                    idx = bisect.bisect_left(nums2, t)
                    cnt += (n2 - idx)
            return cnt

        # search space for products: can be as low as min(nums1)*max(nums2)
        lo, hi = -10**10, 10**10
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
