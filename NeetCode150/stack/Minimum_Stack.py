# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1

"""
    定義一個類別 MinStack
    建立這個類別的物件後，可以操作 push/pop/top/getMin
    ex: s = MinStack()
"""                                     
class MinStack:                              
    """
        __init__ 是 Python 中的建構子(constructor)
        當你寫 MinStack() 時，這個函數會自動被呼叫，用來初始化這個類別的屬性。
        self 是 Python 中代表「這個類別的實體(instance)」的變數。
    """
    def __init__(self):                                          
        """
            是在 MinStack 這個類別裡定義「這個物件有一個 stack 屬性，初始值是空的 list」
            ex:  s = MinStack(), self指的就是s這個物件, 所以self.stack = s.stack
        """                                                           
        self.stack = []                             
        #同步記錄最小值, 因為要O(1)
        self.min_stack = []                                    
    def push(self, val: int) -> None:
        self.stack.append(val)
        #如果 min_stack是空的, 或val比目前最小還小, 加入min_stack
        if not self.min_stack or val <= self.min_stack[-1]: 
             self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        #如果彈出的是目前最小的, 也要從min_stack同步移除
        if val == self.min_stack[-1]:
             self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
