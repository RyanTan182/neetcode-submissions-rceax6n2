/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    private int maxValue;

    public int MaxPathSum(TreeNode root) {
        maxValue = int.MinValue;
        MaxPathSumTracker(root);
        return maxValue;
    }

    public int MaxPathSumTracker(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = Math.Max(MaxPathSumTracker(node.left), 0);
        int right = Math.Max(MaxPathSumTracker(node.right), 0);

        int sum = node.val + left + right;
        maxValue = Math.Max(maxValue, sum);

        return node.val + Math.Max(left, right);
    }
}
