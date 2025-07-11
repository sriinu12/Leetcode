class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1) Build next-greater map for nums2
        next_gt = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                smaller = stack.pop()
                next_gt[smaller] = x
            stack.append(x)

        # 2) Answer for nums1 using the map (default -1)
        return [next_gt.get(x, -1) for x in nums1]
        