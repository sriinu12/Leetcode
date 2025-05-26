class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}  # maps number → its index in nums

        for i, x in enumerate(nums):
            comp = target - x
            if comp in index_map:
                return [index_map[comp], i]
            index_map[x] = i

        # By problem guarantee, one solution always exists
        return []
        