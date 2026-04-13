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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // if p and q are both null, return true
        if((p == nullptr) && (q == nullptr)) return true;
        // if either p or q is null, return false
        if((p == nullptr) || (q == nullptr)) return false;
        // check p and q's node value, if not equal return false
        if(p->val != q->val) return false;
        // check left and right subtree
        bool leftresult = isSameTree(p->left, q->left);
        bool rightresult = isSameTree(p->right, q->right);
        return (leftresult && rightresult);
    }
};
