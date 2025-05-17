from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the n x n matrix by 90 degrees clockwise in-place.
        Steps:
          1) Transpose across the main diagonal.
          2) Reverse each row.
        Time: O(n^2), Space: O(1).
        """
        n = len(matrix)
        
        # 1) Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2) Reverse each row
        for row in matrix:
            row.reverse()
