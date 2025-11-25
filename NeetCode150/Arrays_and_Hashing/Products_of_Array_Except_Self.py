#brutal 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            res.append(product)
        return res

#O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #initial array, ex: res = [1, 1, 1, 1]
        #step1: left product
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        #step2: right product
        right = 1
        for i in range(len(nums) - 1, -1, -1):      #backward: range(start, stop, step) 
            res[i] *= right
            right *= nums[i]
        return res
    
"""
| i  | nums[i] | prefix (left)   | res[i]         | left update            |
| - | -------   | ------------- | ----------  | -------------------   |
| 0 | 1           | 1                  | res[0] = 1 | prefix = 1 × 1 = 1   |
| 1 | 2           | 1                  | res[1] = 1 | prefix = 1 × 2 = 2   |
| 2 | 3           | 2                  | res[2] = 2 | prefix = 2 × 3 = 6   |
| 3 | 4           | 6                  | res[3] = 6 | prefix = 6 × 4 = 24 |
"""