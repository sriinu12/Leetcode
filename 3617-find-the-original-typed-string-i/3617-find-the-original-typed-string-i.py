class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Start with 1 (no long-press case)
        count = 1
        # Add one for each extra repeat
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
        return count
        