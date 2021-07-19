class Solution {
    int[][] moves = new int[][]{{1, 2}, {2, 1}, {-1, -2}, {-2, -1}, {-1, 2}, {2, -1}, {1, -2}, {-2, 1}};
    public int minKnightMoves(int x, int y) {
        x = Math.abs(x);
        y = Math.abs(y);
        int[] target = new int[]{x, y};
        int[] start = new int[]{0, 0};
        if (Arrays.equals(target, start)) return 0;
        Set<String> visited = new HashSet<>();
        visited.add("0,0");
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        int result = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curPosition = queue.poll();
                for (int[] move: moves) {
                    int nextX = curPosition[0] + move[0];
                    int nextY = curPosition[1] + move[1];
                    int[] nextPosition = new int[] {nextX, nextY};
                    String nextString = nextX + "," + nextY;
                    if (nextX==x && nextY==y) return result+1;
                    // Arrays.equals(nextPosition, target) works as well as above.
                    if (nextX < -1 || nextY < -1 || visited.contains(nextString)) continue;
                    visited.add(nextString);
                    queue.add(nextPosition);
                }
            }
            result++;
        }
        return -1;
    }
}
