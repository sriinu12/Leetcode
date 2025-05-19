class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        lo,hi = 0, m*n-1
        while lo <= hi:
            mid = (lo + hi)//2
            i,j = divmod(mid,n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
        