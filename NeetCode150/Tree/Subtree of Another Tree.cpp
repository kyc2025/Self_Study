#include <bits/stdc++.h>

using namespace std;

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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // if subRoot is null, return true
        if(subRoot == nullptr) return true;
        // if root is null, return false
        if(root == nullptr) return false;
        //check if the two trees are the same
        if(isSameTree(root, subRoot)) return true;  
        // check if the left or right subtree of root is the same as subRoot
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if(s == nullptr && t == nullptr) return true;
        if(s == nullptr || t == nullptr) return false;
        if(s->val != t->val) return false;
        return isSameTree(s->left, t->left) && isSameTree(s->right, t->right);

    }
};

int main() {

    return 0;
}
