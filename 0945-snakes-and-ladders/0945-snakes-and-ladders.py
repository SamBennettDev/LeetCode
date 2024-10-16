class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def bousToIndex(bous):
            row = ceil(bous / len(board))
            i = len(board) - row
            if row % 2 != 0:
                j = (bous - 1) % len(board)
            else:
                j = (len(board) - ((bous - 1) % len(board))) - 1
            return i, j
                
        queue = [(1, 0)]
        visited = set()
        end_square = len(board)*len(board)

        while queue:
            curr_pos, turns = queue.pop(0)

            for n in range(1, 7):
                new_pos = curr_pos + n
                i, j = bousToIndex(new_pos)

                if board[i][j] != -1:
                    new_pos = board[i][j]

                if new_pos > end_square:
                    break

                if new_pos == end_square:
                    return turns+1
                
                if new_pos not in visited:
                    queue.append((new_pos, turns+1))
                    visited.add(new_pos)

        return -1