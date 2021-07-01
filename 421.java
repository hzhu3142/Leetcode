// Approach 1 bit manipulation

public class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0, mask = 0;
        for(int i = 31; i >= 0; i--){
            mask = mask | (1 << i);
            Set<Integer> set = new HashSet<>();
            for(int num : nums){
                set.add(num & mask);
            }
            int tmp = max | (1 << i);
            for(int prefix : set){
                if(set.contains(tmp ^ prefix)) {
                    max = tmp;
                    break;
                }
            }
        }
        return max;
    }
}


// approach 2 Trie

public class Trie {

	private class Node {

		int data;
		Node[] children;

		public Node(int data) {
			this.data = data;
			this.children = new Node[2];
		}
	}

	private Node root;

	// O(1)
	public Trie() {
		this.root = new Node(-1);
	}

	// O(32)
	public void addWord(int num) {
		Node curr = root;
		for (int i = 30; i >= 0; i--) {
			int mask = 1 << i;
			int bit = num & mask;
			bit = (bit != 0) ? 1 : 0;
			Node temp = curr.children[bit];
			if (temp == null){
				temp = new Node(bit);
                curr.children[bit] = temp;
            }
			curr = temp;
		}
	}

	// O(32)
	public int searchWord(int num) {
		Node curr = root;
		int ans = 0;
		for (int i = 30; i >= 0; i--) {
			int mask = 1 << i;
			int bit = num & mask;
			bit = (bit != 0) ? 1 : 0;
			int toggle = bit ^ 1;
			Node temp = curr.children[toggle];
			if (temp != null) {
				curr = temp;
				ans |= mask;
			} else
				curr = curr.children[bit];
		}
		return ans;
	}

}

// O(n)
// Trie

class Solution {
    public int findMaximumXOR(int[] nums) {
        Trie trie = new Trie();
        int max = 0;
        for (int num : nums)
            trie.addWord(num);

        for (int num : nums) {
            int ans = trie.searchWord(num);
            max = Math.max(ans, max);
        }

        return max;
    }
}
