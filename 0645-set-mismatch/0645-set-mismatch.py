class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        # Ideal sums for 1..n
        S = n * (n + 1) // 2
        Q = n * (n + 1) * (2*n + 1) // 6

        P = 0        # actual sum of nums
        R2 = 0       # actual sum of squares

        for x in nums:
            P  += x
            R2 += x*x

        delta = P - S             # R - M
        sigma = R2 - Q            # R^2 - M^2

        # R + M = sigma / delta
        sum_RM = sigma // delta

        # Solve: R = ( (R-M) + (R+M) ) / 2
        R = (delta + sum_RM) // 2
        M = R - delta

        return [R, M]