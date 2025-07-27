class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 1) Split and convert to int lists
        levels1 = [int(x) for x in version1.split('.')]
        levels2 = [int(x) for x in version2.split('.')]
        
        # 2) Pad the shorter list with zeros
        n1, n2 = len(levels1), len(levels2)
        if n1 < n2:
            levels1.extend([0] * (n2 - n1))
        elif n2 < n1:
            levels2.extend([0] * (n1 - n2))
        
        # 3) Compare level by level
        for v1, v2 in zip(levels1, levels2):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        # 4) All levels equal
        return 0
        