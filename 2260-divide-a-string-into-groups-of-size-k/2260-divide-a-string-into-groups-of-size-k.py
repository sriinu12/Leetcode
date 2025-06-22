class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups: List[str] = []
        for i in range(0, len(s), k):
            chunk = s[i : i + k]
            # pad if needed
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            groups.append(chunk)
        return groups
        