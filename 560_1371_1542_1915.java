// 560
class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum = 0, result = 0;
        Map<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0, 1);
        for (int num: nums) {
            sum += num;
            result += preSum.getOrDefault(sum-k, 0);
            int cnt = preSum.getOrDefault(sum, 0);
            preSum.put(sum, cnt+1);
        }
        return result;
        
    }
}


// 1371
class Solution {
    public int findTheLongestSubstring(String s) {
        int res = 0 , cur = 0, n = s.length();
        HashMap<Integer, Integer> seen = new HashMap<>();
        seen.put(0, -1);
        for (int i = 0; i < n; ++i) {
            cur ^= 1 << ("aeiou".indexOf(s.charAt(i)) + 1 ) >> 1;
            seen.putIfAbsent(cur, i);
            res = Math.max(res, i - seen.get(cur));
        }
        return res;
    }
}

// 1542
class Solution {
    public int longestAwesome(String s) {
        int res = 0, cur = 0, n = s.length(), seen[] = new int[1024];
        Arrays.fill(seen, n);
        seen[0] = -1;
        for (int i = 0; i < n; ++i) {
            cur ^= 1 << (s.charAt(i) - '0');
            for (int a = 0; a < 10; ++a)
                res = Math.max(res, i - seen[cur ^ (1 << a)]);
            res = Math.max(res, i - seen[cur]);
            seen[cur] = Math.min(seen[cur], i);
        }
        return res;
    }
}

// 1915
class Solution {
    public long wonderfulSubstrings(String word) {
        long res = 0, count[]  = new long[1024];
        int cur = 0;
        count[0] = 1L;
        for (int i = 0; i < word.length(); ++i) {
            cur ^= 1 << (word.charAt(i) - 'a');
            res += count[cur]++;
            for (int j = 0; j < 10; ++j)
                res += count[cur ^ (1 << j)];
        }
        return res;
    }
}






