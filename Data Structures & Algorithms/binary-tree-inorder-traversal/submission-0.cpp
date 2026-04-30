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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res = {};
        this->rec(root, res);
        return res;
    }

private:
    void rec(const TreeNode* node, vector<int>& res) {
        if (node == nullptr) return;
        this->rec(node->left, res);
        res.push_back(node->val);
        this->rec(node->right, res);
    }
};