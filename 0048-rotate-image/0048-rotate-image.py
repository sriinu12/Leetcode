class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left, right = 0, n - 1
        while left < right:
            top, bottom = left, right
            for k in range(right - left):
                # save top-left
                tl = matrix[top][left + k]
                # bottom-left -> top-left
                matrix[top][left + k] = matrix[bottom - k][left]
                # bottom-right -> bottom-left
                matrix[bottom - k][left] = matrix[bottom][right - k]
                # top-right -> bottom-right
                matrix[bottom][right - k] = matrix[top + k][right]
                # top-left(saved) -> top-right
                matrix[top + k][right] = tl
            left += 1
            right -= 1
        """
        Do not return anything, modify matrix in-place instead.
        """
        