class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
                ans += run
            else:
                run = 0
        return ans
        