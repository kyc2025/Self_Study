class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            s = set()           #建立一個空的集合set, 裡面不能有重複的元素, 而且查詢是否存在相當快
            for  num in nums:
                if num in s:
                    return True
                else:
                    s.add(num)
            return  False
"""
    nums: List[int] 參數 nums, 它是一個 list, 而且裡面的元素是 int
    list[int] 等同於 C 的 int* tokens[]
    ex: tokens = [4,13,5]
"""  