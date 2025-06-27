class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # 1. Pre-filter characters that appear ≥ k times
        freq = Counter(s)
        possible = sorted(c for c, cnt in freq.items() if cnt >= k)

        # 2. BFS over candidate subsequences
        ans = ""
        q = deque([""])

        while q:
            curr = q.popleft()
            for ch in possible:
                cand = curr + ch
                # 3. Check if cand * k is subsequence of s
                if self._is_k_subseq(s, cand, k):
                    q.append(cand)
                    # 4. Update answer if longer or lex‐larger
                    if (len(cand) > len(ans)) or (len(cand) == len(ans) and cand > ans):
                        ans = cand

        return ans

    def _is_k_subseq(self, s: str, cand: str, k: int) -> bool:
        i, n = 0, len(s)
        for _ in range(k):
            for ch in cand:
                while i < n and s[i] != ch:
                    i += 1
                if i == n:
                    return False
                i += 1
        return True
        