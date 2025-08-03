class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        if not fruits:
            return 0
        
        # 1. Build a dense 'amounts' array up to the farthest fruit/rightmost index
        maxRight = max(startPos, fruits[-1][0])
        amounts = [0] * (maxRight + 1)
        for pos, cnt in fruits:
            amounts[pos] = cnt
        
        # 2. Build prefix sum so prefix[i+1] = sum(amounts[0..i])
        prefix = list(itertools.accumulate(amounts, initial=0))
        
        # Helper: total fruits in [startPos-leftSteps, startPos+rightSteps]
        def getFruits(leftSteps: int, rightSteps: int) -> int:
            L = max(0, startPos - leftSteps)
            R = min(maxRight, startPos + rightSteps)
            return prefix[R + 1] - prefix[L]
        
        ans = 0
        # Case 1: go right first, then back left
        for right in range(min(maxRight - startPos, k) + 1):
            left = max(0, k - 2 * right)
            ans = max(ans, getFruits(left, right))
        
        # Case 2: go left first, then back right
        for left in range(min(startPos, k) + 1):
            right = max(0, k - 2 * left)
            ans = max(ans, getFruits(left, right))
        
        return ans
        