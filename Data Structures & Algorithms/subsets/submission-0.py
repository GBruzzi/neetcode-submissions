class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        path = []
        res = []

        def bt(index):
            if index == len(nums):
                res.append(path.copy())
                return

            path.append(nums[index])
            bt(index + 1)

            path.pop()
            bt(index + 1)

        bt(0)

        return res