class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1) Quick length check
        if len(s) != len(t):
            return False
        
        # 2) Fixed‐size counter for 'a' to 'z'
        counts = [0] * 26
        
        # 3) Count up for s, down for t
        for ch_s, ch_t in zip(s, t):
            counts[ord(ch_s) - ord('a')] += 1
            counts[ord(ch_t) - ord('a')] -= 1
        
        # 4) Verify all zeros
        for cnt in counts:
            if cnt != 0:
                return False
        
        return True
        