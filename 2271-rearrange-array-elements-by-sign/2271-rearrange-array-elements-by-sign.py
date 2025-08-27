class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pi, ni = 0, 1  # positive goes to even indices, negative to odd
        for x in nums:
            if x > 0:
                res[pi] = x
                pi += 2
            else:
                res[ni] = x
                ni += 2
        return res
        