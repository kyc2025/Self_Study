#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
// maxDiameter是global variable，height函数每次递归都会更新maxDiameter的值
        height(root, maxDiameter);
        return maxDiameter;
    }
    // The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    // This path may or may not pass through the root.
    
private:
    int height(TreeNode* node, int& maxDiameter) {
        if (!node) return 0;
// check left and right subtree's height
    int left = height(node->left, maxDiameter);
    int right = height(node->right, maxDiameter);
// update maxDiameter everytime if left + right is greater than current maxDiameter
        maxDiameter = std::max(maxDiameter, left + right);
        return std::max(left, right) + 1;
    }
};
