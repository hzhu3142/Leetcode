class Solution {

    final Map<String, Boolean> cache = new HashMap<>();

    public boolean isScramble(final String s1, final String s2) {
        if (s1.equals(s2)) return true; 
        
        int[] letters = new int[26];
        for (int i=0; i<s1.length(); i++) {
            letters[s1.charAt(i)-'a']++;
            letters[s2.charAt(i)-'a']--;
        }
        for (int i=0; i<26; i++) if (letters[i]!=0) return false;
    

        String key = s1+"____"+s2;

        if (cache.containsKey(key)) {
            return cache.get(key);
        }

        for (int i = 1; i < s1.length(); i++) {
            final String s2SubstringLeft = s2.substring(0, i);
            final String s2SubstringRight = s2.substring(i);

            if ((isScramble(s1.substring(0, i), s2SubstringLeft)
                    && isScramble(s1.substring(i), s2SubstringRight)) ||
                    (isScramble(s1.substring(s1.length() - i), s2SubstringLeft)
                            && isScramble(s1.substring(0, s1.length() - i), s2SubstringRight))) {

                cache.put(key, true);
                return true;
            }
        }

        cache.put(key, false);
        return false;
    }
}    
