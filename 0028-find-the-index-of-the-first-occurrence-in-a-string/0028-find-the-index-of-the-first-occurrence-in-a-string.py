class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. Edge case: empty needle
        if needle == "":
            return 0

        n, m = len(haystack), len(needle)
        # 2. Slide window of size m over haystack
        for i in range(n - m + 1):
            # 3. Compare substring to needle
            if haystack[i : i + m] == needle:
                return i

        # 4. No occurrence found
        return -1
        