class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS
            n = len(nums)
            # try all unordered pairs i < j
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    rest = [nums[k] for k in range(n) if k != i and k != j]

                    # generate possible results; for + and * we only need one order
                    candidates = [
                        a + b,
                        a * b,
                        a - b,
                        b - a
                    ]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(rest + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])
        