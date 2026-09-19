class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n 

        prefix[0] = nums[0]
        postfix[n -  1] = nums[n - 1]

        for i in range(n):
            if i == 0:
                continue
            prefix[i] = nums[i] * prefix[i - 1]

            postfix[n - 1 - i] = nums[n - 1 - i] * postfix[n - i]

        res = [1] * n 
        res[0] = 1 * postfix[1]
        res[n - 1] = 1 * prefix[n - 2]

        for i in range(1,n - 1,1):
            res[i] = prefix[i - 1] * postfix[i + 1]

        return res