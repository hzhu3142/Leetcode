// 463
class Solution {
    public int islandPerimeter(int[][] grid) {
        int neighbors = 0, count = 0;
        for (int i = 0; i < grid.length; i++ ) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    count++;
                    if (i > 0 && grid[i-1][j] == 1) neighbors++;
                    if (j > 0 && grid[i][j-1] == 1) neighbors++;
                }
            }
        }
        return count * 4 - neighbors * 2;

    }
}

//1254
class Solution {
    int[][] grid;
    int[][] directions = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int closedIsland(int[][] grid) {
        this.grid = grid;
        int m = grid.length, n = grid[0].length;
        int count = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 0 && isClose(i, j)) count++;
            }
        }
        return count;
    }


    public Boolean isClose(int i, int j) {
        int m = grid.length, n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n) return false;
        if (grid[i][j] == 1) return true;
        grid[i][j] = 1;

        Boolean result = true;
        for (int k = 0; k < 4; k++) {
            int a = directions[k][0] + i;
            int b = directions[k][1] + j;
            Boolean check = isClose(a, b);
            result = check && result;
        }

        return result;
    }
}

// 695

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++)
                if(grid[i][j] == 1)max_area = Math.max(max_area, AreaOfIsland(grid, i, j));
        return max_area;
    }

    public int AreaOfIsland(int[][] grid, int i, int j){
        if( i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == 1){
            grid[i][j] = 0;
            int up = AreaOfIsland(grid, i-1, j);
            int left = AreaOfIsland(grid, i, j-1);
            int right = AreaOfIsland(grid, i, j+1);
            int down = AreaOfIsland(grid, i+1, j);
            return 1 + up + left + right + down;
        }
        return 0;
    }
}
