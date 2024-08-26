class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        def start_row_and_col(diag):
            # on col = 0
            if diag < m:
                col = 0
                row = m-1 - diag

            # row = 0
            else:
                row = 0
                col = diag - m+1

            return row, col

        for diag in range(m + n - 1):
            temp = []

            row, col = start_row_and_col(diag)

            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1

            temp.sort(reverse=True)

            row, col = start_row_and_col(diag)

            while row < m and col < n:
                mat[row][col] = temp.pop()
                row += 1
                col += 1

        return mat