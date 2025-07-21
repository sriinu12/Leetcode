class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []              # list to build resulting characters
        count = 0             # consecutive count for the current character
        prev = ''             # previous character seen

        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1
            # Only append if this is not the 3rd in a row
            if count < 3:
                res.append(c)

        return "".join(res)
        