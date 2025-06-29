class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Precompute powers of 2 modulo MOD
        pow2 = [1] * n
        for k in range(1, n):
            pow2[k] = (pow2[k-1] * 2) % MOD

        ans = 0
        i, j = 0, n - 1

        while i <= j:
            if nums[i] + nums[j] <= target:
                # All subsequences using nums[i] as min and any of nums[i+1..j]
                ans = (ans + pow2[j - i]) % MOD
                i += 1
            else:
                # Too large with nums[j], try a smaller max
                j -= 1

        return ans
        