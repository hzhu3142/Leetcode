//200
class Solution {
    char[][] grid;
    int[][] moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int m, n;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        int res = 0;
        m = grid.length;
        n = grid[0].length;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1') {
                    res += 1;
                    grid[i][j] = '0';
                    buryIsland(i, j);
                }
            }

        }
        return res;
    }

    public void buryIsland(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            for (int[] move: moves) {
                int newX = position[0] + move[0];
                int newY = position[1] + move[1];
                if (newX < 0 || newX >= m || newY < 0 || newY >= n ) continue;
                if (grid[newX][newY] == '0') continue;
                grid[newX][newY] = '0';
                queue.add(new int[]{newX, newY});
            }
        }
    }
}

//305

class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {

        List<Integer> res = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        int temp = 0;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        DisjoinSet djs = new DisjoinSet(m*n);
        for (int[] pos: positions) {
            int cell = pos[0] * n + pos[1];
            if (!visited.contains(cell)) {
                temp++;
                visited.add(cell);
                for (int[] dir: directions) {
                    int newX = dir[0] + pos[0];
                    int newY = dir[1] + pos[1];
                    if (newX < 0 || newX >= m || newY < 0 || newY >= n) continue;
                    int newCell = newX * n + newY;
                    if (visited.contains(newCell)) {
                        if (!djs.isConnected(cell, newCell)) {
                            temp--;
                            djs.union(cell, newCell);
                        }
                    }
                }

            }
            res.add(temp);
        }
        return res;

    }

    public class DisjoinSet {
        int[] parents;
        public DisjoinSet(int size) {
            parents = new int[size];
            for (int i = 0; i < size; i++) {
                parents[i] = i;
            }
        }

        private int find(int x) {
            while (x != parents[x]) {
                x = find(parents[x]);

            }
            return parents[x];
        }


        public boolean isConnected(int x, int y) {
            if (find(x) == find(y)) return true;
            return false;
        }

        public void union(int x, int y) {
            int parentX = find(x);
            int parentY = find(y);
            parents[parentX] = parentY;
        }

    }
}
