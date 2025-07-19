class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            # Expand while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After the loop, left/right have gone one too far
            return right - left - 1  # length of palindrome

        for i in range(len(s)):
            len1 = expand_around_center(i, i)     # odd-length
            len2 = expand_around_center(i, i + 1) # even-length
            curr_len = max(len1, len2)

            if curr_len > (end - start + 1):
                # compute new start/end from the center i
                start = i - (curr_len - 1) // 2
                end   = i + curr_len // 2

        return s[start:end + 1]
        