class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # l vai terminar no minimo
        while l < r:
            meio = (l + r) // 2

            if nums[meio] > nums[r]:
                l = meio + 1
            else:
                r = meio

        if target > nums[-1]:
            r = l - 1
            l = 0
        else:
            r = len(nums) - 1

        while l <= r:
            meio = (l + r) // 2

            if nums[meio] == target:
                return meio
            elif nums[meio] > target:
                r = meio - 1
            else:
                l = meio + 1


        return -1