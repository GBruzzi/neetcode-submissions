class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            complemento = target - nums[i]
    
            if complemento in d:
                return [d[complemento], i]
    
            d[nums[i]] = i

            



        return 0