class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        diag_order = []

        row = 0
        col = 0

        num_diags = m + n - 1

        for i in range(num_diags):
            # diag going up right
            if i % 2 == 0:
                while row >= 0 and col < n:
                    diag_order.append(mat[row][col])
                    row -= 1
                    col += 1

                # overshot row
                if col < n:
                    row = 0

                # overshot col
                else:
                    row += 2
                    col = n-1

            # diag going down left
            else:
                while row < m and col >= 0:
                    diag_order.append(mat[row][col])
                    row += 1
                    col -= 1

                # overshot col
                if row < m:
                    col = 0

                # overshot row
                else:
                    col += 2
                    row = m-1
                
        return diag_order