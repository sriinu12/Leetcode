class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            # Try to go deeper in the lexicographical tree (append a '0' digit).
            if curr * 10 <= n:
                curr *= 10
            else:
                # If we can't go deeper, try to increment.
                # If we're at the end (curr == n or last digit is '9'), we need to backtrack.
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result
        