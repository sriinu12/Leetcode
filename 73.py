from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix) , len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        # Explanation:
#         We reuse the first row and first column as our marker arrays.

# Scan first row & first column separately to see if they themselves need zeroing.

# Scan the rest of the matrix (1…m-1, 1…n-1): whenever matrix[i][j]==0, set matrix[i][0]=0 and matrix[0][j]=0.

# Zero rows/cols based on these markers (again for 1…m-1, 1…n-1).

# Finally, zero the first row/column if needed.
        # Time Complexity: O(m*n)
        # Space Complexity: O(1)    