class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)

        res = []

        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            
            target = -nums[i]

            l = i + 1
            r = n - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    triplete = [nums[i], nums[l], nums[r]]
                    res.append(triplete)
                    
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l +=1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1

                else:
                    r -= 1



        return res
