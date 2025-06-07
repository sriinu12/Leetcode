class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        # buckets[c] will store a stack of indices where character c appears
        buckets = {chr(ord('a') + i): [] for i in range(26)}
        # removed[i] == True means we delete s[i]
        removed = [False] * n

        for i, ch in enumerate(s):
            if ch == '*':
                # mark the '*' itself for removal
                removed[i] = True
                # find the smallest letter (from 'a' to 'z') that appeared before
                for c in map(chr, range(ord('a'), ord('z') + 1)):
                    if buckets[c]:
                        idx = buckets[c].pop()   # most recent occurrence
                        removed[idx] = True      # remove that letter
                        break
            else:
                # record this letter’s index
                buckets[ch].append(i)

        # build the final string from all characters not marked removed
        result = []
        for i, ch in enumerate(s):
            if not removed[i]:
                result.append(ch)
        return "".join(result)
        