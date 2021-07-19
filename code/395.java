/* Credit: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/170010/Java-O(n)-Solution-with-Detailed-Explanation-Sliding-Window
 * Pattern: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
 * O(26 * n) ~ O(n)
 *
 * Basically iterate through the number of possible unique letters 1 to 26. Lets
 * call our target amount of unique letters u. We search all windows of letters
 * where the number of unique letters <= u. This is the number of any unique
 * letters, not the number of unique letters that occur k or more times. We
 * count the number of current unique letters, and the number of letters that
 * have a count of k or more using a sliding window.
 */
class Solution {
    public int longestSubstring(String s, int k) {
        int d = 0;

        for (int uniqueCharsTarget = 1; uniqueCharsTarget <= 26; uniqueCharsTarget++)
            d = Math.max(d, longestSubstringWithNUniqueChars(s, k, uniqueCharsTarget));

        return d;
    }

    private int longestSubstringWithNUniqueChars(String s, int k, int uniqueCharsTarget) {
        int[] map = new int[128];
        int uniqueChars = 0; // counter 1 to count number of unique chars
        int charsKorMoreCount = 0; // counter 2 to count chars with k or more count
        int begin = 0, end = 0;
        int d = 0;

        while (end < s.length()) {
            char endChar = s.charAt(end);

            /*
             * We expand, if our number of unique letters is less than or equal to
             * uniqueCharsTarget, we need to add a letter, so we increment the right
             * pointer, and add the count of the right letter by 1. If the count is equal to
             * 0 we know this is a new letter so we increment unique, and if it is equal to
             * k we increment charsKorMoreCount since it just became k or more.
             *
             * Note that the reason we choose this route if it's equal is that we need to
             * keep expanding the letters if its at the target uniqueCharsTarget because we
             * can still have a chance at getting more charsKorMoreCount letters and
             * uniqueChars == uniqueCharsTarget.
             *
             * For example, aaabb if we stop at "a" since uniqueChars == uniqueCharsTarget (1=1) we won't ever
             * get to "aaa" which is the answer.
             */
            // if curr freq is 0 we incr the uniqueChars items and curr elem's freq in the
            // map
            if (map[endChar] == 0) {
                uniqueChars++;
            }
            map[endChar]++;
            // if curr freq reached k we incr the charsKorMoreCount items
            if (map[endChar] == k) {
                charsKorMoreCount++;
            }
            end++;

            /*
             * We shorten, if our number of unique letters is more than uniqueCharsTarget ,
             * we need to remove a letter, so we decrement the left pointer, and decrease
             * the count of the left letter by 1. If the count is equal to 0 we decrement
             * the number of unique letters since all instances of this letter are gone, if
             * it's equal to k it is now not k or more so we decrement charsKorMoreCount.
             */
            while (uniqueChars > uniqueCharsTarget) {
                char beginChar = s.charAt(begin);

                if (map[beginChar] == k) {
                    charsKorMoreCount--;
                }
                map[beginChar]--;

                if (map[beginChar] == 0) {
                    uniqueChars--;
                }
                begin++;
            }

            // if we found a string where the number of unique chars equals our target
            // and all those chars are repeated at least K times then update max
            if (uniqueChars == uniqueCharsTarget && uniqueChars == charsKorMoreCount)
                d = Math.max(end - begin, d);
        }

        return d;
    }
}
