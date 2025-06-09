class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int) -> int:
            """
            Count how many numbers between `prefix` and `prefix+1` 
            (in lexicographical tree) are ≤ n.
            """
            nxt = prefix + 1
            count = 0
            # Expand down each level of the “trie”
            while prefix <= n:
                count += min(n + 1, nxt) - prefix
                prefix *= 10
                nxt    *= 10
            return count

        curr = 1
        k -= 1  # we start at “1”, so decrement k

        # Walk the lexicographical tree until we've advanced k steps
        while k > 0:
            cnt = count_prefix(curr)
            if cnt <= k:
                # Skip entire subtree under curr
                k   -= cnt
                curr += 1
            else:
                # Go deeper into curr’s subtree
                k    -= 1
                curr *= 10

        return curr

        