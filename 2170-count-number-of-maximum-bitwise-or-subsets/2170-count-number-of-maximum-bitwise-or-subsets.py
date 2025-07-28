class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # dp[or_val] = number of subsets seen so far with OR = or_val
        dp = {0: 1}
        for x in nums:
            new_dp = dp.copy()
            for or_val, cnt in dp.items():
                new_or = or_val | x
                new_dp[new_or] = new_dp.get(new_or, 0) + cnt
            dp = new_dp

        # global max OR is the OR of all elements
        max_or = 0
        for x in nums:
            max_or |= x

        # subtract 1 if you want to exclude the empty subset;
        # but dp[max_or] only counts non‑empty contributions because
        # empty subset remains at OR=0, not max_or (unless max_or==0).
        return dp.get(max_or, 0)
        