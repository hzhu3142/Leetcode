// 130
class Solution {

    char[][] board;
    int[][] directions = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};

    public void solve(char[][] board) {
        this.board = board;
        int m = board.length, n = board[0].length;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (i==0 || i==m-1 || j==0 || j==n-1) {
                    if (board[i][j] == 'O') {
                        convert(i, j);
                    }
                }
            }
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == 'W') board[i][j] = 'O';

            }
        }

    }

    public void convert(int i, int j) {
        int m = board.length, n = board[0].length;
        board[i][j] = 'W';
        for (int k = 0; k < 4; k++) {
            int x = directions[k][0] + i;
            int y = directions[k][1] + j;
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] != 'O') continue;
            convert(x, y);
        }
    }
}


// 934
class Solution {
    public int shortestBridge(int[][] A) {
        int m = A.length, n = A[0].length;
        boolean[][] visited = new boolean[m][n];
        int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Queue<int[]> q = new LinkedList<>();
        boolean found = false;
        // 1. dfs to find an island, mark it in `visited`
        for (int i = 0; i < m; i++) {
            if (found) {
                break;
            }
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    dfs(A, visited, q, i, j, dirs);
                    found = true;
                    break;
                }
            }
        }
        // 2. bfs to expand this island
        int step = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int[] cur = q.poll();
                for (int[] dir : dirs) {
                    int i = cur[0] + dir[0];
                    int j = cur[1] + dir[1];
                    if (i >= 0 && j >= 0 && i < m && j < n && !visited[i][j]) {
                        if (A[i][j] == 1) {
                            return step;
                        }
                        q.offer(new int[]{i, j});
                        visited[i][j] = true;
                    }
                }
            }
            step++;
        }
        return -1;
    }
    private void dfs(int[][] A, boolean[][] visited, Queue<int[]> q, int i, int j, int[][] dirs) {
        if (i < 0 || j < 0 || i >= A.length || j >= A[0].length || visited[i][j] || A[i][j] == 0) {
            return;
        }
        visited[i][j] = true;
        q.offer(new int[]{i, j});
        for (int[] dir : dirs) {
            dfs(A, visited, q, i + dir[0], j + dir[1], dirs);
        }
    }
}

// 827
