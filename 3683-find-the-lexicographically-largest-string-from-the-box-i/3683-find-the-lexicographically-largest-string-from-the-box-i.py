class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Return the lexicographically largest substring that can appear when
        splitting `word` into exactly `numFriends` non-empty parts,
        across all possible splits.
        """
        n = len(word)
        # If there's only one friend, the only valid split is the entire string.
        if numFriends == 1:
            return word
        
        # k is the maximum chunk length: n − numFriends + 1
        k = n - numFriends + 1

        # Step 1: find the start index of the lexicographically maximum suffix
        start = self._max_suffix_index(word)
        
        # Step 2: take the substring of length k (or until the end of the string)
        end = min(start + k, n)
        return word[start:end]

    def _max_suffix_index(self, s: str) -> int:
        """
        Find the index i such that s[i:] is the lexicographically maximum suffix of s.
        This runs in O(n) time using a two-pointer approach.
        """
        n = len(s)
        i, j, k = 0, 1, 0
        
        while j + k < n and i < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            
            if s[i + k] > s[j + k]:
                # s[i:] > s[j:], skip the region starting at j
                j = j + k + 1
            else:
                # s[j:] > s[i:], move i up to j, and skip region at i
                new_i = j
                j = max(j + 1, i + k + 1)
                i = new_i
            
            k = 0
        
        return i
