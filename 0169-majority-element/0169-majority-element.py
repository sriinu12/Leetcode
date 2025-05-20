class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None
        for x in nums:
            if count == 0:

                cand = x
            count += 1 if x == cand else -1
        return cand
        