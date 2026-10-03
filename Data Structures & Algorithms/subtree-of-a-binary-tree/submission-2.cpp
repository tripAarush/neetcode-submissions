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
    bool check(TreeNode* node, TreeNode* copy){
        if (!node and !copy){
            return true;
        }
        if (!node or !copy){
            return false;
        }
        if (node->val == copy->val and check(node->left, copy->left) and check(node->right, copy->right)){
            return true;
        }
        return false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root){
            return false;
        }
        if (check(root,subRoot)){
            return true;
        }
        if (isSubtree(root->left,subRoot) || isSubtree(root->right,subRoot)){
            return true;
        }
        return false;
    }
};
