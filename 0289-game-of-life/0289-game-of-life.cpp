class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        vector<vector<int>> dir = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1},
                                   {0, 1},   {1, -1}, {1, 0},  {1, 1}};

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                int liveNeighbors = 0;
                for (int k = 0; k < 8; k++) {
                    int x = dir[k][0] + i;
                    int y = dir[k][1] + j;

                    if (x >= 0 && x < board.size() && y >= 0 &&
                        y < board[i].size() && board[x][y] % 2) {
                        liveNeighbors++;
                    }
                }
                if (board[i][j]) { // is alive
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = 3;
                    }
                } else { // is dead
                    if (liveNeighbors == 3) {
                        board[i][j] = 4;
                    }
                }
            }
        }
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                board[i][j] = board[i][j] % 3;
            }
        }
    }
};