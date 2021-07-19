// Approach 1: create hash map <Character, String[]> + queue

class Solution {
    static Map<Character, String[]> num2char = new HashMap<>();
    // if there is no static, the instance variable of hashmap can't be constructed.
    static {
        num2char.put('2', new String[]{"a", "b", "c"});
        num2char.put('3', new String[]{"d", "e", "f"});
        num2char.put('4', new String[]{"g", "h", "i"});
        num2char.put('5', new String[]{"j", "k", "l"});
        num2char.put('6', new String[]{"m", "n", "o"});
        num2char.put('7', new String[]{"p", "q", "r", "s"});
        num2char.put('8', new String[]{"t", "u", "v"});
        num2char.put('9', new String[]{"w", "x", "y", "z"});
    }
    // if the hashmap is initilized inside the method below, no static needed.

    public List<String> letterCombinations(String digits) {
        int size = digits.length();
        if (size == 0) return Arrays.asList(); // be careful about the corner case.

        Queue<String> queue = new LinkedList<>();
        queue.add("");

        for (int i = 0; i < size; i++) {
            Queue<String> newQueue = new LinkedList<>();
            while (!queue.isEmpty()) {
                String cur = queue.poll();
                for (String letter: num2char.get(digits.charAt(i))) {
                    newQueue.add(cur + letter);
                }
            }
            queue = new LinkedList<>(newQueue); // deep copy an existing queue;
        }

        return (List) queue;
        // return Arrays.asList(queue); this code doesn't work, inside the bracket, it should be an Array.
    }
}

// Approach2: create hashMap <Character, String> + queue
class Solution {
    Map<Character, String> num2char = new HashMap<>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};


    public List<String> letterCombinations(String digits) {
        int size = digits.length();
        if (size == 0) return Arrays.asList(); // be careful about the corner case.

        Queue<String> queue = new LinkedList<>();
        queue.add("");

        for (int i = 0; i < size; i++) {
            Queue<String> newQueue = new LinkedList<>();
            while (!queue.isEmpty()) {
                String cur = queue.poll();
                String nextCandidates = num2char.get(digits.charAt(i));
                for (int j=0; j < nextCandidates.length(); j++) {
                    char letter = nextCandidates.charAt(j);
                    newQueue.add(cur + letter);
                }
            }
            queue = new LinkedList<>(newQueue); // deep copy an existing queue;
        }

        return (List) queue;
        // return Arrays.asList(queue); this code doesn't work, inside the bracket, it should be an Array.
    }
}



// Approach3 Create an array + queue.
class Solution {
    static String[] num2char = new String[10];
    static{
        num2char[2] = "abc";
        num2char[3] = "def";
        num2char[4] = "ghi";
        num2char[5] = "jkl";
        num2char[6] = "mno";
        num2char[7] = "pqrs";
        num2char[8] = "tuv";
        num2char[9] = "wxyz";
        // num2char[9] = new String "wxyz"; this one doesn't work.
    }
    // If the array is inside the method below. don't need static.


    // String[] num2char = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    // String[] num2char = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        // The two ways above work fine as well;

    public List<String> letterCombinations(String digits) {
        int size = digits.length();
        if (size == 0) return Arrays.asList(); // be careful about the corner case.

        Queue<String> queue = new LinkedList<>();
        queue.add("");

        for (int i = 0; i < size; i++) {
            Queue<String> newQueue = new LinkedList<>();
            while (!queue.isEmpty()) {
                String cur = queue.poll();
                String nextCandidates = num2char[digits.charAt(i) - '0'];
                for (int j = 0; j < nextCandidates.length(); j++ ) {
                    newQueue.add(cur + nextCandidates.charAt(j));
                }
                // for (Char ch: nextCandidates) this code doesn't work.

                // for (char letter : num2char[digits.charAt(i) - '0'].toCharArray()) {
                //     newQueue.add(cur + letter);
                // } // this for loop works fine to convert String to a list of characters.
            }
            queue = new LinkedList<>(newQueue); // deep copy an existing queue;
        }

        return (List) queue;
        // return Arrays.asList(queue); this code doesn't work, inside the bracket, it should be an Array.
    }
}


// Approach4: Create an array + Arraylist

class Solution {

    String[] num2char = new String[] {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        int size = digits.length();
        if (size == 0) return Arrays.asList(); // be careful about the corner case.

        List<String> result = new ArrayList<>();
        result.add("");

        for (int i = 0; i < size; i++) {
            List<String> temp = new ArrayList<>();

            for (String cur: result) {
                String nextCandidates = num2char[digits.charAt(i) - '0'];
                for (int j = 0; j < nextCandidates.length(); j++ ) {
                    temp.add(cur + nextCandidates.charAt(j));
                }
            }
            result = temp;
        }

        return result;
    }
}
