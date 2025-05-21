class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for x in nums:
            if cand1 is not None and x == cand1:
                cnt1 += 1
            elif cand2 is not None and x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = x, 1
            elif cnt2 == 0:
                cand2, cnt2 = x, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

    # 2) Verification
        result = []
        threshold = len(nums) // 3
    # Count actual frequencies
        actual1 = actual2 = 0
        for x in nums:
            if x == cand1:
                actual1 += 1
            elif x == cand2:
                actual2 += 1

        if actual1 > threshold:
            result.append(cand1)
        if actual2 > threshold:
            result.append(cand2)

        return result