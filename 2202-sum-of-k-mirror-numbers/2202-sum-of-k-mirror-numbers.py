class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # helper: is s a palindrome?
        def is_pal(s: str) -> bool:
            return s == s[::-1]

        # helper: convert x>0 into base-k string
        def to_base_k(x: int) -> str:
            if x == 0:
                return "0"
            digits = []
            while x > 0:
                digits.append(str(x % k))
                x //= k
            return "".join(reversed(digits))

        total = 0
        found = 0
        L = 1

        while found < n:
            # determine how many digits in the "half" we need
            half_len = (L + 1) // 2
            start = 10 ** (half_len - 1)
            end   = 10 ** half_len

            for half in range(start, end):
                s = str(half)
                # build exactly-L-digit palindrome
                if L % 2 == 0:
                    pal = int(s + s[::-1])
                else:
                    # mirror all but the last digit of s
                    pal = int(s + s[-2::-1])

                # check its base-k representation
                if is_pal(to_base_k(pal)):
                    total += pal
                    found += 1
                    if found == n:
                        return total

            L += 1

        return total
        