class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1  # empty prefix
        s = 0
        ans = 0
        for x in nums:
            s += x
            ans += freq[s - k]
            freq[s] += 1
        return ans
        