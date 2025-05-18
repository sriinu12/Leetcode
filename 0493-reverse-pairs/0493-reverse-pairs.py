class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_count(left: int, right: int) -> int:
            # Sort nums[left:right], return count of reverse pairs
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            cnt = sort_count(left, mid) + sort_count(mid, right)

            # Count pairs across the split
            j = mid
            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - mid

            # In-place merge of two sorted halves
            temp = []
            i, k = left, mid
            while i < mid and k < right:
                if nums[i] <= nums[k]:
                    temp.append(nums[i]); i += 1
                else:
                    temp.append(nums[k]); k += 1
            temp.extend(nums[i:mid])
            temp.extend(nums[k:right])
            nums[left:right] = temp

            return cnt

        return sort_count(0, len(nums))
        