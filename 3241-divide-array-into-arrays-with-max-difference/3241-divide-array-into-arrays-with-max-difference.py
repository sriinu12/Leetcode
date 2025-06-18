class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # sort the array first :contentReference[oaicite:0]{index=0}
        ans: List[List[int]] = []
        n = len(nums)

        for i in range(2, n, 3):
            # Check the max difference in this triplet
            if nums[i] - nums[i - 2] > k:
                return []
            ans.append([nums[i - 2], nums[i - 1], nums[i]])

        return ans
        