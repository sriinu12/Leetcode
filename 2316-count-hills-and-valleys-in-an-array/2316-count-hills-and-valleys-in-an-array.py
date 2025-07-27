class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        ans = 0
        prev = nums[0]

        i = 1
        while i < n - 1:
            # Skip if same as left neighbor (flat region continuation)
            if nums[i] == nums[i - 1]:
                i += 1
                continue

            # Find the next distinct element to the right
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            if j == n:  # no right neighbor
                break

            # Check hill or valley
            if (nums[i] > prev and nums[i] > nums[j]) or \
               (nums[i] < prev and nums[i] < nums[j]):
                ans += 1

            # Move prev to the current block’s value and advance
            prev = nums[i]
            i += 1

        return ans
        