class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            value = numbers[l] + numbers[r]

            if target == value:
                return [l + 1,r + 1]
            elif target < value:
                r -= 1
            else:
                l += 1