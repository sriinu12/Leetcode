class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diag_sq = -1
        best_area = -1
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > best_diag_sq or (diag_sq == best_diag_sq and area > best_area):
                best_diag_sq = diag_sq
                best_area = area
        return best_area
        