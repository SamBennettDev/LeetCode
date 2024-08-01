function numIslands(grid: string[][]): number {
    let islands: number = 0;

    function dfs(x: number, y: number) {
        if (x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] !== '1') {
            return;
        }

        grid[x][y] = "0";

        dfs(x - 1, y);
        dfs(x + 1, y );
        dfs(x, y - 1);
        dfs(x, y + 1);
    }

    for (let i: number = 0; i < grid.length; i++) {
        for (let j: number = 0; j < grid[i].length; j++) {
            if (grid[i][j] != "1") continue;

            dfs(i, j);
            islands += 1; 
        }
    }

    return islands;
};