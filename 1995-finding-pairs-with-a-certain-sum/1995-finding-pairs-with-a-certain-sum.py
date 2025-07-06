class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Store the arrays
        self.nums1 = nums1
        self.nums2 = nums2
        # Build a frequency map of nums2
        self.count2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        # Remove old value
        old = self.nums2[index]
        self.count2[old] -= 1
        # Update nums2 and frequency
        self.nums2[index] = old + val
        self.count2[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        # For each x in nums1, we need nums2[j] == tot - x
        ans = 0
        for x in self.nums1:
            ans += self.count2.get(tot - x, 0)
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)