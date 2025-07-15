class Solution:
    def isValid(self, word: str) -> bool:
        # 1) Minimum length
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        vowels = set("aeiouAEIOU")

        for c in word:
            # 2) Only letters or digits allowed
            if not c.isalnum():
                return False

            # 3) Track vowels vs consonants
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        # 4) Must have at least one of each
        return has_vowel and has_consonant
        