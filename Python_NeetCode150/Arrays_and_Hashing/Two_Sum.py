class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}     #用 dict 存「數字 -> index」

        for i, num in enumerate(nums): #它讓你「同時」取得：
                                                                #i: 目前的 index
                                                                #num: 目前的元素值
            left = target - num
            if left in seen:
                return [seen[left], i] 
            seen[num]=i
        """
            nums = [10,20,30]
            for i, num in enumerate(nums):
            print(i, num)
            
            output:
                0 10
                1 20
                2 30
            C: 
            for (int i = 0; i < len; i++) 
            {
                num = nums[i];
                printf("%d %d\n", i, num);
            }
        """    
#