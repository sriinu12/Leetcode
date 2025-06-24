class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans: List[int] = []
        j = 0

        for i in range(n):
            # Move j to the first key at or beyond i - k
            while j < n and (nums[j] != key or j < i - k):
                j += 1
            if j == n:
                break
            # If that key is within k of i, record i
            if abs(i - j) <= k:
                ans.append(i)

        return ans
        