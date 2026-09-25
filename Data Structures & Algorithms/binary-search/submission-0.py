class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            meio = (l + r)// 2
            el = nums[meio]

            if target == el:
                return meio
            elif target < el:
                r = meio - 1
            else:
                l = meio + 1

        return -1