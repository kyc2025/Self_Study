class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
                tokens: List[str] 參數 tokens, 它是一個 list, 而且裡面的元素是 string。
                list[str] 等同於 C 的 char* tokens[]
                ex: tokens = ["4", "13", "5", "/", "+"]
        """    
        stack = []
        for token in tokens:
            """
                只要遇到數字就先塞入堆疊, 若是符號, 就需pop出來最上層兩個數字, 運算完再塞進Stack中
            """    
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token =='/':
                    stack.append(int(a/b))  #int(2.6) = 2
        return stack[0]