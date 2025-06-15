class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)
        
        # Build a: replace first non-'9' with '9'
        # If all are '9', this leaves `a = num`.
        for ch in s:
            if ch != '9':
                a = int(s.replace(ch, '9'))
                break
        else:
            a = num
        
        # Build b:
        # Case 1: first digit isn't '1' → replace it with '1'
        if s[0] != '1':
            b = int(s.replace(s[0], '1'))
        else:
            # Case 2: first digit is '1' → look for first ch in s[1:] not in {'0','1'}
            for ch in s[1:]:
                if ch not in ('0', '1'):
                    b = int(s.replace(ch, '0'))
                    break
            else:
                # No suitable digit found → no change
                b = num
        
        return a - b
        