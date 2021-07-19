class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));


        if (deadSet.contains(target) || deadSet.contains("0000") ) return -1;
        if (target.equals("0000")) return 0;

        Queue<String> queue = new LinkedList<>();
        queue.add("0000");
        Set<String> visited = new HashSet<>();
        int result = 0;
        int[] changes = new int[]{1, 9};
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                for (int j = 0; j < 4; j++) {
                    for (int change: changes) {
                        int num = (cur.charAt(j) - '0' + change) % 10; // don't need to convert num to string.
                        String newPassword = cur.substring(0, j) + num + cur.substring(j+1, 4);
                        if (newPassword.equals(target)) return result + 1;
                        if (visited.contains(newPassword) || deadSet.contains(newPassword))  continue;
                        visited.add(newPassword);
                        queue.add(newPassword);
                    }

                }

            }
            result++;

        }
        return -1;
    }
}
