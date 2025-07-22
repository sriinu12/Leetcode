class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        current_sum = 0
        max_sum = 0

        for j, x in enumerate(nums):
            # If x is duplicate in window, shrink from left until duplicate removed
            while x in seen:
                # remove nums[i] from window
                seen.remove(nums[i])
                current_sum -= nums[i]
                i += 1
            # add new element
            seen.add(x)
            current_sum += x
            # update max
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
        