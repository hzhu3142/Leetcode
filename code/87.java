class Solution {

    final Map<String, Boolean> cache = new HashMap<>();  // final: can't change??

    public boolean isScramble(final String s1, final String s2) {
        
        String key = s1+s2;

        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        
        if (s1.equals(s2)) return true; 
        
        int[] freq = new int[26];
        for (int i=0; i<s1.length(); i++) {
            freq[s1.charAt(i)-'a']++;
            freq[s2.charAt(i)-'a']--;
        }
        for (int i=0; i<26; i++) if (freq[i]!=0) return false;

        for (int i = 1; i < s1.length(); i++) {
            
            final String s1left = s1.substring(0, i);
            final String s1right = s1.substring(i);
            final String s2left = s2.substring(0, i);
            final String s2right = s2.substring(i);

            if (isScramble(s1left, s2left)
                    && isScramble(s1right, s2right)) {
                cache.put(key, true);
                return true;
            }
            
            if  (isScramble(s1right, s2.substring(0, s1.length() - i))
                            && isScramble(s1left, s2.substring(s1.length() - i))) {

                cache.put(key, true);
                return true;
            }
        }

        cache.put(key, false);
        return false;
    }
}       
