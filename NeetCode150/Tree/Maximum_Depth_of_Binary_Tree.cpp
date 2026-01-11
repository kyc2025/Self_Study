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
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
            return 0;
        // 1 node = 1+ left/right tree's max     
        return (1 + max(maxDepth(root->left), maxDepth(root->right)));
    }
};
    //     3
    //    / \
    //   9  20
    //      / \
    //     15  7
// from bottom to top
// The depth of a tree is one plus the maximum depth of its left and right subtrees
//
// maxDepth(15) = 1
// maxDepth(7) = 1
// maxDepth(20) = 1 + max(1, 1) = 2
// maxDepth(9) = 1
// maxDepth(3) = 1 + max(1, 2) = 3