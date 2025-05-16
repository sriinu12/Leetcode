from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        parent = [-1] * n
        def hamming(a: str, b: str) -> int:
            diff = 0
            for x, y in zip(a,b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return 2
            return diff
        best_len = 1
        best_end = 0
        for j in range(n):
            for i in range(j):
                if(
                    groups[i] != groups[j]
                    and len(words[i]) == len(words[j])
                    and hamming(words[i], words[j]) == 1
                ):
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        parent[j] = i
                        if dp[j] > best_len:
                            best_len = dp[j]
                            best_end = j
        res = []
        idx = best_end
        while idx != -1:
            res.append(words[idx])
            idx = parent[idx]
        return res[::-1]
# # # Explanation:
# Explanation of Key Steps
# DP Array:

# dp[i] holds the length of the longest valid subsequence ending at index i.

# We initialize all to 1 (the word itself).

# Parent Pointers:

# parent[i] stores the previous index in the subsequence for backtracking.

# Hamming Distance Check:

# We only allow transitions from i→j if groups[i] != groups[j], the same length, and Hamming distance = 1.

# Nested Loop (O(n²·L)):

# For each j, scan all i < j to update dp[j] and parent[j] when valid.

# Tracking the Best:

# Keep best_len and best_end so we know where the LIS ends.

# Reconstruction:

# Starting from best_end, follow parent[] back to -1, collecting words in reverse order, then reverse to correct.