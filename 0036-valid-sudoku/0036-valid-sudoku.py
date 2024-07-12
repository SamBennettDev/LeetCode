class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_contains = [0] * 9
            col_contains = [0] * 9

            for j in range(9):
                # Validate Rows
                if (board[i][j] != "."):
                    if (row_contains[int(board[i][j]) - 1] != 0):
                        return False

                    row_contains[int(board[i][j]) - 1] = 1

                # Validate Cols
                if (board[j][i] != "."):
                    if (col_contains[int(board[j][i]) - 1] != 0):
                        return False

                    col_contains[int(board[j][i]) - 1] = 1

                # Validate Blocks
                if (i % 3 == 0 and j % 3 == 0):
                    block_contains = [0] * 9
                    for m in range(3):
                        for n in range(3):
                            if (board[i + m][j + n] != "."):
                                if (block_contains[int(board[i + m][j + n]) - 1] != 0):
                                    return False

                                block_contains[int(board[i + m][j + n]) - 1] = 1

        return True