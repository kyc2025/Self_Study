"""
        Backtracking (Recursive)
        Backtracking 是一種試探法：先試一個可能的選擇，再根據狀況回頭修正路徑（也就是「回溯」）。

        一個字串是合法的括號組合需滿足：
        1. 在任何位置，左括號的數量都大於等於右括號, 例如不能有 ")("
        2. 最後必須 左右括號各有 n 個
"""    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
                定義一個函數backtrack(current, open_count, close_count)
                current_string: 目前生成的字串
                left: 已使用的左括號數量
                right: 已使用的右括號數量
        """        
        res = []
        def backtrack(current: str, left: int, right: int):
                """
                        剪枝條件(pruning)
                        如果左括號用完了，就不能再加 '('
                        如果右括號的數量 > 左括號，表示字串不合法
                """
                if left == n and right == n:
                     res.append(current)
                     return
                    # ✂️ 剪枝 1：左括號還可以加
                if left < n:
                        backtrack(current + '(', left + 1, right)

                    # ✂️ 剪枝 2：右括號只能在比左括號少的情況下加
                if right < left:
                        backtrack(current + ')', left, right + 1)

        backtrack("", 0, 0)
        return res






class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        for i in range(n):
                stack.append("()")