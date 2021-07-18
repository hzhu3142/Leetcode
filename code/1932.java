/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
//   collect all child nodes in trees
    Set<Integer> children = new HashSet<>();  
  
    public TreeNode canMerge(List<TreeNode> trees) {
          
        Map<Integer, TreeNode> value2tree = new HashMap<>();
        
        for (TreeNode t: trees) {
            value2tree.put(t.val, t);
            if (t.left != null) children.add(t.left.val);
            if (t.right != null) children.add(t.right.val);
        }
        
        TreeNode root = null;
        for (TreeNode t: trees) {
            if ( !children.contains(t.val)) {
                if (root != null) return null; // return null if find a second value that is not in children.
                root = t;
            }
        }
        
        if (root == null) return null;
        
        for (TreeNode t: trees) {
            
            if (t.left != null && value2tree.containsKey(t.left.val)) {
                TreeNode node = value2tree.get(t.left.val);
                t.left = node;
            }
            
            if (t.right != null && value2tree.containsKey(t.right.val)) {
                TreeNode node = value2tree.get(t.right.val);
                t.right = node;
            }
        }
        
        if (validBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE)) { 
         
            if (children.isEmpty())  return root;
        } 
         
        return null;
    
    }
    
//   check valid binary search tree
    private boolean validBST(TreeNode root, int left, int right) {
        if (root == null) return true;
        
        if (children.contains(root.val)) children.remove(root.val);
        
        if (root.val <= left || root.val >= right) return false;
        
        boolean l = validBST(root.left, left, root.val);
        boolean r = validBST(root.right, root.val, right);
        
        return l && r;
        
    }
    
}
