from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Return the longest subsequence of `words` such that no two
        consecutive chosen words come from the same group.
        """
        ans = []
        prev_group = None
        
        for w, g in zip(words, groups):
            # Always take the first word, or take when group changes
            if prev_group is None or g != prev_group:
                ans.append(w)
                prev_group = g
        
        return ans
# # Explanation:
# # The function getLongestSubsequence takes a list of words and their corresponding groups.
# Explanation of Key Steps
# Initial Setup:

# We keep a variable prev_group to remember the group ID of the last included word.

# We accumulate results in the list ans.

# Greedy One-Pass:

# Index 0: Always include words[0], set prev_group = groups[0].

# For i = 1…n−1:

# If groups[i] != prev_group, include words[i] and update prev_group.

# Otherwise skip it.

# Correctness:
# Since we only need to avoid two consecutive picks with the same group, this picks the maximum possible elements (greedy), in O(n) time.

# Space Complexity:
# Aside from the output list (size up to n), we use O(1) extra space.

# This solves the problem in a single pass with minimal overhead.