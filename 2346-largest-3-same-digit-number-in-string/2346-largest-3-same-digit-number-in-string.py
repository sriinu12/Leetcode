class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""  # store the best 3-char substring
        for i in range(len(num) - 2):
            a, b, c = num[i], num[i+1], num[i+2]
            if a == b == c:
                if not best or a > best[0]:
                    best = a * 3
        return best
