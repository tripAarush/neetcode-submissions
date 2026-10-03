/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int res = 0;
    int dfs(TreeNode* node){
        if (!node){
            return 0;
        }
        int leftH = 0, rightH = 0;
        if (node->left){
            leftH = dfs(node->left) + 1;
        }
        if (node->right){
            rightH = dfs(node->right) + 1;
        }
        res = max(res, leftH + rightH);
        return max(leftH, rightH);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return res;
    }
};
