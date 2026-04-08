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
    bool isBalanced(TreeNode* root) {
        int result = checkHeight(root);
        if (result==-1)
            return false;
        else
            return true;
    }

private: 
    int checkHeight(TreeNode* root)
    {        
        if(root==NULL)
            return 0;
        int leftheight=checkHeight(root->left);
        // 如果左節點已經發現不平衡，直接傳回 -1 表示失敗。
        if (leftheight == -1) return -1;

        int rightheight=checkHeight(root->right);
        // 右節點本身不平衡，就直接告訴上一層「整棵樹不平衡」。
        if (rightheight == -1) return -1;

        // 左右子樹高度差如果大於 1，就代表這個節點的樹不平衡。
        if(abs(leftheight-rightheight)>1)
            return -1;

        // 如果左右子樹都沒問題，回傳這個節點的高度：比較高的那邊加 1。
        return max(leftheight, rightheight) + 1;
    }
};