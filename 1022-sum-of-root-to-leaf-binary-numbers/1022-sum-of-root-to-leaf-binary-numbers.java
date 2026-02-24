/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int sumRootToLeaf(TreeNode root) {
        return calculateSum(root, 0);
    }

    private int calculateSum(TreeNode node, int currentSum) {
        // Base case: if the node is null, contribute nothing to the sum
        if (node == null) {
            return 0;
        }

        // Update the current path sum: 
        // Bitwise shift left (currentSum * 2) and add the node's value
        currentSum = (currentSum << 1) | node.val;

        // If it's a leaf node, return the completed binary value
        if (node.left == null && node.right == null) {
            return currentSum;
        }

        // Otherwise, recurse through left and right children
        return calculateSum(node.left, currentSum) + calculateSum(node.right, currentSum);
    }
}