class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)
        if n < 4:
            return res

        nums.sort()

        for i in range(n - 3):
            # Skip duplicate first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Early termination: smallest possible sum
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Early continue: largest possible sum too small
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            for j in range(i+1, n - 2):
                # Skip duplicate second element
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # Early termination for this j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # Early continue if sum too small
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                lo, hi = j + 1, n - 1
                while lo < hi:
                    s = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if s < target:
                        lo += 1
                    elif s > target:
                        hi -= 1
                    else:
                        # Found a quadruplet
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        # Skip duplicates for lo and hi
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -= 1

        return res