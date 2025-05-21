class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything; modify matrix in-place.
        If an element is 0, set its entire row and column to 0.
        Uses O(1) extra space by using first row/column as markers.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        # Step 1: Determine if first row or first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 2: Use first row & column as markers for other rows/cols
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Zero out cells based on markers in first row/column
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Step 4: Finally zero first row and/or first column if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0