class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # 1) sort by x asc, y desc
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0

        # 2) fix i as top-left; sweep j to the right
        for i, (_, yi) in enumerate(points):
            maxY = -math.inf  # highest y we've already accepted for this i
            for j in range(i + 1, len(points)):
                yj = points[j][1]
                if yi >= yj and yj > maxY:
                    ans += 1
                    maxY = yj
        return ans
        