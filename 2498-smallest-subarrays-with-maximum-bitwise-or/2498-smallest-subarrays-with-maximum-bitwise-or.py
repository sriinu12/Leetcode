class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # latest[j] = farthest index to the right where bit j was seen
        latest = [0] * 30

        # scan from right to left
        for i in range(n - 1, -1, -1):
            # for each bit position
            for j in range(30):
                # check if bit j is set in nums[i]
                if (nums[i] >> j) & 1:
                    latest[j] = i
                # else, if we've seen this bit later, we must reach it
                elif latest[j] > i:
                    ans[i] = max(ans[i], latest[j] - i + 1)
        return ans
        