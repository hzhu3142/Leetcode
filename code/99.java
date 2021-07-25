// method 1 stack
class Solution {
    public void recoverTree(TreeNode root) {
        TreeNode swap1=null, swap2=null, prev=null, cur;
        Stack<TreeNode> stack = new Stack<>();
        // Deque<TreeNode> stack = new LinkedList<>(); this line works as well.
        cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur!= null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (prev != null && prev.val > cur.val) {
                if (swap1 == null) {
                    swap1 = prev;
                    swap2 = cur;
                } else {
                    swap2 = cur;
                    break;
                }
            }
            prev = cur;
            cur = cur.right;
        }
        int temp = swap1.val;
        swap1.val = swap2.val;
        swap2.val = temp;
    }
}

// method 2 recursion

class Solution {
    TreeNode val1 = null, val2 = null;
    TreeNode min = null;
    public void recoverTree(TreeNode root) {
        walk(root);
        int tmp = val1.val;
        val1.val = val2.val;
        val2.val = tmp;
    }
    private void walk(TreeNode curr){
        if(curr == null) return;
        walk(curr.left);
        if(min != null && curr.val < min.val){
            if(val1 == null){
                val1 = min;
                val2 = curr;
            }else
                val2 = curr; //override previous val2 since there are only two misplaced elems
        }
        min = curr;
        walk(curr.right);
    }
}
