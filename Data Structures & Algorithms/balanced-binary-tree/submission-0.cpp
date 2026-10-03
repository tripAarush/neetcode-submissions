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
    tuple<int,bool> dfs(TreeNode* node){
        if (!node){
            return tuple<int, bool> (0, true);
        }
        int left_h = 0, right_h = 0;
        if (node->right) {
            auto[r_h, valid] = dfs(node->right);
            if (!valid){
                return tuple<int,bool> (-1, false);
            }
            right_h = r_h+1;
        }
        if (node->left) {
            auto[l_h, valid] = dfs(node->left);
            if (!valid){
                return tuple<int,bool> (-1, false);
            }
            left_h = l_h+1;
        }

        if (abs(left_h - right_h) > 1){
            return tuple<int,bool> (-1, false);
        }
        return tuple<int,bool> (max(left_h, right_h), true);
    }
    bool isBalanced(TreeNode* root) {
        return get<1>(dfs(root));
    }
};
