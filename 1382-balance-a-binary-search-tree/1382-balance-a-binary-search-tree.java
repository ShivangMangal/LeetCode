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
    List<TreeNode> nodes = new ArrayList<>();
    public TreeNode balanceBST(TreeNode root) {
        inorder(root);
        return build(0, nodes.size() - 1);
    }
    // Step 1: Inorder traversal
    private void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        nodes.add(root);
        inorder(root.right);
    }
    // Step 2: Build balanced BST
    private TreeNode build(int left, int right) {
        if (left > right) return null;
        int mid = (left + right) / 2;
        TreeNode root = nodes.get(mid);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
}
