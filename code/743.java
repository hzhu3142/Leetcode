class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
        
        int size = times.length;
        for(int i=0; i<size; i++) {
            int node1 = times[i][0];
            int node2 = times[i][1];
            int distance = times[i][2];
            Map<Integer, Integer> temp = new HashMap<>();
            graph.putIfAbsent(node1, temp);
            graph.get(node1).put(node2, distance);
        }
        
        boolean[] visited = new boolean[n+1];
        int res = 0;
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        pq.add(new int[]{0, k});
        
        while (!pq.isEmpty()) {
            int[] temp = pq.poll();
            int distance = temp[0];
            int node = temp[1];
            if (visited[node]) continue;
            visited[node] = true;
            res = distance;
            n--;
            if (n==0) break;
            if (graph.containsKey(node)) {
                for (int nextNode: graph.get(node).keySet()) {
                    int nextDistance = graph.get(node).get(nextNode);
                    pq.add(new int[]{nextDistance+distance, nextNode});
                }
            }
            
        }
        return n == 0? res:-1;
    }
}
