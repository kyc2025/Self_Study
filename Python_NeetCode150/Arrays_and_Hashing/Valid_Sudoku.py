#brutal force method
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #set 3 data structure to record
        rows = [set() for _ in range(9)]  #set a list contained 9 element, every element is set() and is empty to restore differnet element
                                                         #[set(), set(), set(), set(), set(), set(), set(), set(), set()]
                                                         #ex: rows[0].add(5):
                                                         #[{5}, set(), set(), set(), set(), set(), set(), set(), set()]
        cols =  [set() for _ in range(9)]  
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":          #skip .
                    continue

                box_index = (r // 3) * 3 + (c // 3)
                """
                ->ROW:向下新增, column:向右新增
                        c0 c1 c2 c3 c4 c5 c6 c7 c8
                r0  [ 5  3  . | .  7  . | .  .  . ]  ← row 0
                r1  [ 6  .  . | 1  9  5 | .  .  . ]  ← row 1
                r2  [ .  9  8 | .  .  . | .  6  . ]  ← row 2
                box_index: 
                        0 1 2
                        3 4 5
                        6 7 8
                r // 3: represent what Row box (0,1,2)
                //:整數除法(floor division): 只保留整數, 不要小數點
                rows 0,1,2 -> r//3 = 0(up)
                rows 3,4,5 -> r//3 = 1(middle)
                rows 6,7,8 -> r//3 = 2(down)
                """
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
